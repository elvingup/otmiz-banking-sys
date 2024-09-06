Otimização da [simulação de sistema bancário](arquivo-original.py)

    objetivo geral {
        
        separar as funções existentes de saque, depósito e extrato em funções.
        
        criar duas funções novas, quais sejam [
            cadastrar usuário, i.e., o cliente 
            cadastrar conta bancária 

        ]
    }

    objetivos específicos {

        modularizar o código[
            criar funções para as[ 
                
                § operações existentes [
                    sacar (
                        essa função recebe argumentos keyword only
                    )

                    depositar(
                        essa função recebe argumentos positional only
                    )

                    extrato(
                        essa função recebe argumentos[
                            positional only para o saldo 

                            keyword only para o extrato 
                        ]
                    )
                ]

                § operações novas [
                    criar usuário, i.e., cliente do banco(
                        § essa função armazena os usuários em uma lista 

                        § o usuário é composto por [
                            nome 
                            data de nascimento 
                            CPF [
                                armazena apenas os numerais e remove outros caracteres 

                                número inteiro que é único no sistema 
                            ]
                            endereço [
                                string que registra [
                                    logradouro 
                                    número 
                                    bairro 
                                    cidade
                                    sigla do estado 
                                ]
                            ]
                        ]
                    )
                    
                    criar conta corrente vinculada ao usuário(
                        § essa função armazena contas em uma lista 

                        § a conta corrente é composta por [
                            agência[
                                § há apenas uma agência, qual seja: 0001

                                § o  número da agência é armazenada como tipo  string 
                            ]
                            número da conta [
                                único no sistema 
                            ]
                            usuário [
                                § o usuário pode ter mais de uma conta corrente 

                                § cada conta corrente se relaciona a  apenas um usuário 

                                § para vincular um usuário a alguma conta corrente [
                                    filtre a lista de usuário ao buscar pelo CPF respectivo ao usuário 
                                ]
                            ]
                        ]
                    )
                ]
            ]
        ]
    }
