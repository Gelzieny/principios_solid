class Programmer:
  def make_code(self):
    print("Programmer creating code")

class Seller:
  def make_code(self):
    print("Seller selling the products")

class Company:
  def do_work(self, worker: any) -> None:
    worker.make_code()

programmer = Programmer()
company = Company()
seller = Seller()

company.do_work(programmer)
company.do_work(seller)
