class room:
    def __init__(self,id,beds,price,vip,claimed,start_date,end_date,claimer_name):
        self.id = id
        self.beds = beds
        self.price = price
        self.vip = vip
        self.claimed = claimed
        self.start_date = start_date
        self.end_date = end_date
        self.claimer_name = claimer_name
    
    def default_values():
        return {
            "id" : " ",
            "beds" : 0,
            "price" : 0.0,
            "vip" : 0,
            "claimed" : 0,
            "start_date" : " ",
            "end_date" : " ",
            "claimer_name" : " "
        }

# id;beds;price;vip;claimed;start_date;end_date;claimer_name