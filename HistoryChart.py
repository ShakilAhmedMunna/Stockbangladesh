import re


class HistoryChart:
    def __init__(self , dseUrl):
        self.soup = dseUrl
        #self.help = Help.Help()


    def historyChart(self):
        script = self.soup.findAll("script")

        for Index , h in enumerate(script):
            #print(Index , "    " , h)
            if(Index == 15):
                self.row = "\n".join([i.strip()  for i in h])
                #self.row = str(self.row).replace('[',' ').replace(']',' ').replace('{',' ').replace('}',' ').replace('+',' ').replace(':',' ').replace('{',' ').replace('chart7 = new Highcharts.Chart','')
                self.arr = " ".join(self.row.split(':'))
                #print(re.split('; |, |\*|\n',self.arr))
                self.arr =re.split('; ( | ) | { | } |, | = | | , | |\*|\n',self.arr)
                #self.arr = re.split('\n|,\t,\r,',self.arr)
                print(type(self.arr))
                for index , j in enumerate(self.arr):
                    print( "[ " , index , " ] ",j)
