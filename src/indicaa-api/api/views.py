from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from scraping.QtdeAlunosMatriculados import alunosPorDisciplina
from .serializers import MateriaSerializer, UnidadeSerializer, TurmaSerializer
from .services import IndicaaServices
from .models import Materia, Unidade, Turma


class UnidadeViewSet(viewsets.ModelViewSet):
    def get(self, request):
        resultado = alunosPorDisciplina()
        turma=[]
        materia = []
        indicaa = IndicaaServices()
        for item in resultado["materia"]:
            for i in item["turmas"]:
                turma.append(TurmaSerializer(
                    professor=i["professor"],
                    codigoTurma=i["codigoTurma"],
                    vagasOcupadas= i.vagasOcupadas,
                    vagasOfertadas=i.vagasOfertadas,
                    local=i.local,
                    horario=i.horario,
                    semestre=i.semestre,
                    ano=i.ano
                ))
            materia.append(MateriaSerializer(
                nome=item.nome,
                codigoMaterias=item.codigoMateria,
                turmas=turma
            ))
            indicaa.criar_materia(materia)
        unidade = UnidadeSerializer(
            nome=resultado.nome,
            materia=materia
        )
        
        
    queryset = Unidade.objects.all().order_by('nome')
    serializer_class = UnidadeSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all().order_by('codigoMateria')
    serializer_class = MateriaSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all().order_by('materia')
    serializer_class = TurmaSerializer
