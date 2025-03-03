class Process:
  def handle(self, username: str, password: str) -> None:
    if self.__verify_input_data(username, password):
      self.__verify_input_data(username)
      self.__insert_user(username, password)
        
    else:
      self.__raise_error('Dados inválidos')
    
  def __verify_input_data(self, username: str, password: str) -> bool:
    return isinstance(username, str) and isinstance(password, str)
  
  def __verify_input_data(self, username: str) -> None:
    print('Acessando o banco de dados...')
    print('Verificando existencia do usuário...')

  def __insert_user(self, username: str, password: str) -> None:
    print('Cadastro de usuário realizado com sucesso!')

  def __raise_error(self, message: str) -> Exception:
    raise Exception('Dados inválidos')