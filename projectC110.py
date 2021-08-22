import plotly.figure_factory as ff
import pandas as pd
import statistics as stat
import plotly.graph_objects as go
import random 

df = pd.read_csv("medium_data.csv")

average_list = df["average"].tolist()
mean = stat.mean(df["average"].tolist())
s = stat.stdev(df["average"].tolist())
print(mean)
print(s)

def sample():
    random_data = []
    for i in range(0,100):
        random_index = random.randint(0, len(average_list)-1)
        value = average_list[random_index]
        random_data.append(value)
    return stat.mean(random_data)

def main():
    m_list = []
    for i in range(0,1000):
        m = sample()
        m_list.append(m)
    
    sample_std = stat.stdev(m_list)
    sample_mean = stat.mean(m_list)
    print("The standard devination for sample data mean is, ",sample_std)
    print("The sample data mean is, ",sample_mean)

    fig = ff.create_distplot([m_list], ["plot for sample averages"], show_hist = False)
    fig.show()
main()
