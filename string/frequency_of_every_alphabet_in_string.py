st='banana'
reg=''
for ch in st:
    if ch not in reg:
        print(f'{ch}:{st.count(ch)}')
    reg=reg+ch
