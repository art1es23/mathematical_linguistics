import pickle

import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

from django.shortcuts import render
import os
from django.conf import settings
from django.db.models import Case, When
from django.http import JsonResponse

from django.db.models import Q
from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer


import pandas as pd
# Create your views here.


class Top3Teachers(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        ml_model = getattr(settings, 'DEFINE_TEACHER_MODEL', 'the_default_value')
        vectorizer = getattr(settings, 'VECTORIZER', 'the_default_value')
        labelencoder = getattr(settings, 'LABELENCODER', 'the_default_value')
        text_to_recognize = [self.request.query_params.get('text')]
        probs_of_teachers = ml_model.predict_proba(
            vectorizer.transform(text_to_recognize))[0]
        top_three = sorted(zip(probs_of_teachers,
                               list(range(len(probs_of_teachers)))),
                           reverse=True)[:3]
        top_three_named = []
        for pair in top_three:
            top_three_named.append(labelencoder.inverse_transform(
                [pair[1]]
            ))

        top_three_named = [item for sublist in top_three_named for item in sublist]
        teachers_ids = [Teacher.objects.get(name=top_three_named[0]).id,
                        Teacher.objects.get(name=top_three_named[1]).id]
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(teachers_ids)])
        return Teacher.objects.filter(pk__in=teachers_ids).order_by(preserved)




