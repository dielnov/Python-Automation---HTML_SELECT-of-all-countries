from bs4 import BeautifulSoup as bs

list = []
i = 0
name_me = ''
with open('fix.html') as htmlFile:
    soup = bs(htmlFile, 'lxml')
    options = soup.find_all('option')
    for option in options:
        original = option
        fit = '{%% if individual.branch == "%s" %%} selected="selected" {%% endif %%}' % (
            option.text)
        name_me = 'countryOfResidence'
        fit = fit.replace('branch', name_me)
        fit = str(option).split(' ')[0] + ' ' + fit

        hold = str(option).split(' ')
        hold[0] = fit

        fitted = ' '.join(hold)
        list.append(fitted)
        i += 1

myfile = open(name_me+'.html', 'w')
for line in list:
    myfile.write(line + '\n')
myfile.close()
