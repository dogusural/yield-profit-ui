
class yield_calculator:

    days_in_year = 365
    total_harvest_fee = 0.29

    def __init__(self, stable_amount, harvest_period, apy_stable, apy_cake, harvest_year=1):
        self.stable_amount = stable_amount
        self.harvest_period = harvest_period
        self.harvest_year=harvest_year
        self.apy_stable = apy_stable/100
        self.apy_cake = apy_cake/100
        self.epoch = yield_calculator.days_in_year / harvest_period * harvest_year

    def calculate(self):
        cake_history = []
        epoch_history = []
        epoch_count = 1
        cake_amount = 0
        while self.epoch > 0:

            if self.epoch < 1 :
                stable_yield = ( self.stable_amount * self.apy_stable / yield_calculator.days_in_year * self.harvest_period * self.epoch) 
                cake_yield = ( cake_amount * self.apy_cake / yield_calculator.days_in_year * self.harvest_period * self.epoch) 
                cake_amount = cake_amount + cake_yield + stable_yield - yield_calculator.total_harvest_fee
                epoch_history.append(int(epoch_count * self.harvest_period - self.harvest_period * self.epoch))
            else :
                stable_yield = ( self.stable_amount * self.apy_stable / yield_calculator.days_in_year * self.harvest_period) 
                cake_yield = ( cake_amount * self.apy_cake / yield_calculator.days_in_year * self.harvest_period) 
                cake_amount = cake_amount + cake_yield + stable_yield - yield_calculator.total_harvest_fee
                epoch_history.append(epoch_count*self.harvest_period)

            cake_history.append(cake_amount)
            epoch_count += 1
            self.epoch = self.epoch - 1
        return(cake_history,epoch_history)






