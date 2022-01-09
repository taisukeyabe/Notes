from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriallizers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method':'GET',
            'body':None,
            'description' : 'Reurns an array of notes',
        },
        {
            'Endpoint': '/notes/id',
            'method':'GET',
            'body':None,
            'description' : 'Reurns a single note object',
        },
        {
            'Endpoint': '/notes/create/',
            'method':'POST',
            'body': {'body':'"'},
            'description' : 'Creates new notes with data sent in post req',
        },
        {
            'Endpoint': '/notes/id/update/',
            'method':'PUT',
            'body': {'body':'"'},
            'description' : 'Creates an existiong notes with data sent in post req',
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description' : 'Delete and exitiong notes',
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes =Note.objects.all()
    seriallizers = NoteSerializer(notes, many=True)
    return Response(seriallizers.data)

@api_view(['GET'])
def getNote(request, pk):
    note =Note.objects.get(id=pk)
    seriallizers = NoteSerializer(note, many=False)
    return Response(seriallizers.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    seriallizers = NoteSerializer(note, many=False)
    return Response(seriallizers.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    seriallizers = NoteSerializer(note, data=request.data)
    if seriallizers.is_valid():
        seriallizers.save()
    return Response(seriallizers.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')