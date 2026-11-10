class Customer:

    def __init__(self, customers = None):
        if customers is None:
            self.customers = []
        else:
            self.customers = customers

    def create_customer(self, name: str, email: str, faturamento_mensal: float) -> dict:
        customer = {
            "name": name,
            "email": email,
            "faturamento_mensal": faturamento_mensal
        }
        self.customers.append(customer)

        return customer

    def is_eligeble_for_pro(self, customer) -> bool:
        if customer['faturamento_mensal'] < 5000:
            return False
        
        return True

    def calculate_annual_revenue(self, customer) -> float:
        return customer['faturamento_mensal'] * 12

    def final_report(self):

        retorno = []
        
        for customer in self.customers:
            retorno.append({
                "Cliente": customer['name'],
                "E-mail": customer['email'],
                "Faturamento Anual": self.calculate_annual_revenue(customer),
                "Plano Elegível": "PRO" if self.is_eligeble_for_pro(customer) else "FREE"
            })
        return retorno