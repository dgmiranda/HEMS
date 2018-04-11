# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
import sqlite3
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
User = get_user_model()


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

def get_data(request, *args, **kwargs):
            table_name = 'readings'
            id_column = 'uniqueID'
            column_2 = 'reading'
            column_3 = 'time_stamp'

            #Open our database
            db = sqlite3.connect('/Users/dgm/Desktop/HEMS_DB')

            #Get a cursor object
            cursor = db.cursor()


            cursor.execute('select * from {tn} '.\
                                format(tn=table_name, cn=id_column))


            all_cunts = cursor.fetchall()

            values=[]

            dates=[]

            ids=[]

            for row in all_cunts:
                    ids.append(str(row[0]))

                    values.append(int(row[1]))
                    ## unicode to string
                    b=str(row[2])
                    ##string to datetime
                    dates.append(datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f'))

            db.commit()
            db.close()

            data = {
                    "id": ids,
                    "readings": values,
                    "date_time": dates,
                    }

            return JsonResponse(data)

class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
            table_name = 'readings'
            id_column = 'uniqueID'
            column_2 = 'reading'
            column_3 = 'time_stamp'

            #Open our database
            db = sqlite3.connect('/Users/dgm/Desktop/HEMS_DB')

            #Get a cursor object
            cursor = db.cursor()


            cursor.execute('select * from {tn} '.\
                                format(tn=table_name, cn=id_column))


            all_cunts = cursor.fetchall()

            values=[]

            dates=[]

            ids=[]

            for row in all_cunts:
                    ids.append(str(row[0]))

                    values.append(int(row[1]))
                    ## unicode to string
                    b=str(row[2])
                    ##string to datetime
                    dates.append(datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f'))

            db.commit()
            db.close()

            data = {
                    "id": ids,
                    "readings": values,
                    "date_time": dates,
                    }
            return Response(data)

def STATS(request):
    return render(request,'HEMS/STATS.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/STATS')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'HEMS/reg_form.html', args)

def home(request):

        table_name = 'readings'
        id_column = 'uniqueID'
        column_2 = 'reading'
        column_3 = 'time_stamp'

        	#Open our database
        db = sqlite3.connect('/Users/dgm/Desktop/HEMS_DB')

        #Get a cursor object
        cursor = db.cursor()


        cursor.execute('select reading, time_stamp from {tn} where {cn} = "cunt"'.\
                            format(tn=table_name, cn=id_column))


        all_cunts = cursor.fetchall()

        values=[]

        dates=[]

        for row in all_cunts:

                values.append(int(row[0]))
                ## unicode to string
                b=str(row[1])
                ##string to datetime
                dates.append(datetime.strptime(b, '%Y-%m-%d %H:%M:%S.%f'))

        args = {'readings': values, 'date_time': dates}

            #print(dates)

        db.commit()
        db.close()

        return render(request,'HEMS/home.html', args)
