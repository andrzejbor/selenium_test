import pandas as pd


def create_excel_file(animal_list, file_path, index_name):
    df_list = []
    index_name.reverse()
    for animal in animal_list:
        df_list.append(pd.DataFrame([animal[1::2]], columns=animal[0::2], index=[index_name.pop()]))

    final_df = pd.concat(df_list)
    final_df.to_excel(file_path)


'''
my_list = [['Domena', 'eukarionty', 'Królestwo', 'zwierzęta', 'Gromada', 'ssaki', 'Podgromada', 'żyworodne', 'Infragromada', 'łożyskowce', 'Nadrząd', 'kopytne', 'Rząd', 'Cetartiodactyla', 'Podrząd', 'wielbłądokształtne', 'Rodzina', 'wielbłądowate', 'Plemię', 'Lamini', 'Rodzaj', 'lama'], ['Domena', 'eukarionty', 'Królestwo', 'zwierzęta', 'Typ', 'kręgowce', 'Gromada', 'ssaki', 'Podgromada', 'żyworodne', 'Infragromada', 'łożyskowce', 'Rząd', 'parzystokopytne', 'Rodzina', 'wołowate', 'Podrodzina', 'koziorożce', 'Rodzaj', 'owca'], ['Domena', 'eukarionty', 'Królestwo', 'zwierzęta', 'Typ', 'strunowce', 'Podtyp', 'kręgowce', 'Gromada', 'ssaki', 'Podgromada', 'żyworodne', 'Infragromada', 'łożyskowce', 'Rząd', 'parzystokopytne', 'Rodzina', 'wołowate', 'Podrodzina', 'koziorożce', 'Rodzaj', 'Capra']]
file_path = 'Animals.xlsx'
index_names = ['a', 'b', 'c']
create_excel_file(my_list, file_path, index_names)
'''
