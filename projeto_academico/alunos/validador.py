import alunos.operacoes as op

def verificar_matricula_existente(matricula):
    for alu in op.alunos:
        if(alu['matricula'] == matricula):
            return True
        
    return False