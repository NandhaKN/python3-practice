fruit_master = ['Orange','apple','mango','grapes','blackberry','cherry']
checkfruits = ['Orange','apple','github',"visualstudio",'grapes']
for fruit in checkfruits:
    if not fruit in fruit_master:
        print (fruit)
