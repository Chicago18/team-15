# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import Http404
from enrollment.models import Parent, Child, Assignments, Users


def index(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def login(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def profile(request,username=""):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def parentHome(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def parentLogin(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def childProfile(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def forms(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})


def enroll(request):
    if request.method == 'GET':
            return render(request, 'enrollment/home.html', {})
