import streamlit as st

def create_interface1():
        size = st.radio('Size', ('So tiny you cant see (1k)', 'The only right option (40k)', 'HUGE (costs your soul)'))
        st.write('☆ More options ☆')
        col3, col4 = st.columns(2)
        with col3:
            milk = st.checkbox('Beef (3.14159k)')
            coffee = st.checkbox('Кофе (8k)')
        with col4:
            cream = st.checkbox('feet cream (10k)')
            eggs = st.checkbox('An entire chicken ()')
        return size, milk, coffee, cream, eggs
def create_interface2():
    col5, col6 = st.columns(2)
    with col5:
        topping = st.multiselect('Topping', ['White boba pearls (999k)', 'Black boba pearls (999k)', 'Jelly (1.5tr)', 'Lychee (858932432041048)', 'Longan (-10k)', 'Peach (???)'])
    with col6:
        amount = st.number_input('How many copies', 1)
    notes = st.text_area('Notes', '''HELLO 
    TEACHER :))
    ~vtpu''')
    return topping, amount, notes

st.title("CotAI Milk Tea (≧∇≦)ﾉ")
col1, col2 = st.columns(2)
with col1:
    st.image('https://collecticontoys.com/cdn/shop/products/transformers-botbot-series5-hibotchi-heats-super-bubs-bubble-tea-drink_1024x1024.jpg?v=1583264897')
    st.text('Hinh anh chi mang tinh chat minh hoa :))))))')
with col2:
    s, m, co, cr, e = create_interface1()
t, n, k = create_interface2()
listOfXtras = []
def calc(are, you, reading, this, right, now):
         # are = size, you = milk, reading = coffee, this = cream, "chicken" (eggs) is gonna be free 😋😋😋, right = topping, now = amount)
        price = 0
        if are =="So tiny you cant see (1k)":
             price += 1
        elif are =="The only right option (40k)":
             price += 40
        elif are == "HUGE (costs your soul)":
             price += 666
        if you == True:
             price += 3.14159
             listOfXtras.append("Beef")
        if reading == True:
             price += 8
             listOfXtras.append("Кофе")
        if this == True:
             price += 10
             listOfXtras.append("feet cream")
        if right.count('White boba pearls (999k)') != 0:
             price += 999
        if right.count('Black boba pearls (999k)') != 0:
             price += 999
        if right.count('Jelly (1.5tr)') != 0:
             price += 1500
        if right.count('Lychee (858932432041048)') != 0:
             price += 858932432041048/1000
        if right.count('Longan (-10k)') !=0:
             price -= 10
        if right.count('Peach (???)') != 0:
             price = price*(-1)
        price = price*now
        return price
def main():
     size, milk, coffee, cream, eggs = s, m, co, cr, e
     topping, amount, notes = t, n, k
     #yes = list(milk, coffee, cream, eggs)
     #listofxtras = [milk, coffee, cream, eggs]
     #listofchosenxtras = []
     #for i in yes:
          #if yes[i] == True:
               #listofchosenxtras.append(listofxtras[i])
     if st.button('ORDER ( •̀ ω •́ )✧', use_container_width=True):
          price = calc(size, milk, coffee, cream, topping, amount)
          if size == 'So tiny you cant see (1k)':
               z = 'So tiny you cant see'
          elif size == 'The only right option (40k)':
               z = 'The only right option'
          else:
               z = 'HUGE'
          st.success(f'''
                    {z}
                   \nExtra: {', '.join(listOfXtras)}
                   \nToppings: {', '.join(topping)}
                   \n{notes}
                   \nAmount: {amount}
                   \nYOUR TOTAL: {price}k
                   ''')
main()