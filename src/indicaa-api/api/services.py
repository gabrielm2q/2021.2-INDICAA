from .models import Unidade, Turma, Materia

class IndicaaServices:

    def criar_unidade(self, unidade):
        unidade = Unidade.objects.filter(nome=unidade.nome).last()
        if(unidade==None):
            unidade = Unidade.objects.create(
                nome=unidade.nome
            )
        return unidade
    def criar_materia(self, materia):
        materia_teste = Materia.objects.filter(codigoMateria=materia.codigoMateria).last()
        if(materia_teste==None):
            materia_teste = Materia.objects.create(
                nome=materia.nome,
                codigoMateria=materia.codigoMateria,
                cargaHoraria="",
                unidade=materia.unidade
            )
            materia_teste.save()
        return materia_teste

    def atualizar_materia(self, codigoMateria, cargahoraria):
        Materia.objects.filter(codigoMateria=codigoMateria).update(cargaHoraria=cargahoraria)

    def criar_turma(self, turma):
        turma_teste = Turma.objects.filter(docente=turma.professor, codigoTurma=turma.codigoTurma).last()
        if(turma_teste==None):
            turma_teste = Turma.objects.create(
                docente=turma.professor,
                codigoTurma=turma.codigoTurma,
                vagasOcupadas=turma.vagasOcupadas,
                vagasOfertadas=turma.vagasOfertadas,
                local=turma.local,
                horario=turma.horario,
                semestre=turma.semestre,
                ano=turma.ano,
                materia=turma.materia
            )
            turma_teste.save()