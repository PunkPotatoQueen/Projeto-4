import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Sales': [200, 300, 400, 350, 500]
}
df = pd.DataFrame(data)

# Criando o gráfico
df.plot(x='Year', y='Sales', kind='line')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()