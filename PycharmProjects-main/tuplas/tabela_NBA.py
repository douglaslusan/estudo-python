nba = ('Philadelphia 76ers','Brooklyn Nets','Milwaukee Bucks','New York Knicks','Atlanta Hawks','Miami Heat',
       'Boston Celtics','Washington Wizards','Indiana Pacers','Charlotte Hornets','Chicago Bulls','Toronto Raptors',
       'Cleveland Cavaliers','Orlando Magic','Detroit Pistons')
# 15 times

# os cinco primeiros colocados
for i in range(0,5):
    print(nba[i])
print('*******************************')
# os ultimos 4 colcados
for i in range(11, len(nba)):
    print(nba[i])
print('*******************************')

# imprimindo em ordem
print(nba)

print('*******************************')

# procurando chigago bulls
for i in range(0, len(nba)):
    if nba[i] == 'Chicago Bulls':
        print(f'esta na {i+1}ª colocacao')




