from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import utilerias

from random import randrange


@api_view(['GET'])
def getAlgoritmos(request):
    lista_de_algoritmos = [
        "Neural Networks",
        "K-nearest neighbors",
        "Naive Bayes",
        "Clusters",
        "Vector Machines",
        "Random forest",
        ]
    return Response(lista_de_algoritmos)

@api_view(['POST'])
def createAlgoritmo(request):
    response = {
        'result': 'Algoritmo creado correctamente',
        'code': 'success'
    }
    return Response(response)

@api_view(['PUT'])
def updateAlgoritmo(request, id):
    response = {
        'result': 'Algoritmo actualizado correctamente',
        'code': 'success'
    }
    return Response(response)

@api_view(['DELETE'])
def deleteAlgoritmo(request, id):
    response = {
        'result': 'Algoritmo eliminado correctamente',
        'code': 'success'
    }
    return Response(response)

@api_view(['POST'])
def ejecutarAlgoritmo(request, id):
    # tomar el CSV que se guardó de otra llamada
    # procesarlo
    resultado1 = utilerias.get_csv_data()
    resultado2 = utilerias.get_csv_data()
    resultado3 = utilerias.get_csv_data()
    
    response = {
        'result': f'Algoritmo {id} ejecutado',
        'csvData': resultado1,
        'urlImg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Niobe050905-Siamese_Cat.jpeg/223px-Niobe050905-Siamese_Cat.jpeg',
        'resultado1': resultado1,
        'resultado2': resultado2,
        'resultado3': resultado3,
        'data': {
            'algo1': {
            "labels": ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
            "datasets": [
                {
                    "label": 'Ganancias',
                    "data": datasetGenerate(),
                    "borderColor": 'rgb(255, 99, 132)',
                    "backgroundColor": 'rgba(255, 99, 132, 0.5)',
                },
                {
                    "label": 'Perdidas',
                    "data": datasetGenerate(),
                    "borderColor": 'rgb(53, 162, 235)',
                    "backgroundColor": 'rgba(53, 162, 235, 0.5)',
                },
            ],
            },
            "algo2": {
            "labels": ['1', '2', '3', '4', '5', '6', '7'],
            "datasets": [
                {
                    "label": 'Ganancias',
                    "data": datasetGenerate(),
                    "borderColor": 'rgb(255, 99, 132)',
                    "backgroundColor": 'rgba(255, 99, 132, 0.5)',
                },
                {
                    "label": 'Perdidas',
                    "data": datasetGenerate(),
                    "borderColor": 'rgb(53, 162, 235)',
                    "backgroundColor": 'rgba(53, 162, 235, 0.5)',
                },
            ],
            }
        },
        'code': 'success'
    }
    return Response(response)

def datasetGenerate():
    return [randrange(1, 100),randrange(1, 100),randrange(1, 100),randrange(1, 100),randrange(1, 100),randrange(1, 100),randrange(1, 100),]