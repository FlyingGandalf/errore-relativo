def errore():
    # ValoreMedio1
    vm1 = input("inserisci un valore medio: ")
    
    # ErroreRelativo1
    ea1 = input("inserisci l'errore assoluto: ")
    
    # ValoreMedio2
    vm2 = input("inserisci il secondo valore medio: ")
    
    # ErroreRelativo2
    ea2 = input("inserisci il secondo errore: ")
    

    # type(input) == str -> converto in int
    vm1 = int(vm1) 
    ea1 = int(ea1) 
    vm2 = int(vm2) 
    ea2 = int(ea2)

    # ProdottoValoriMedi
    pvm = vm1*vm2
    
    #ErroreRelativo1
    er1 = ea1/vm1

    #ErroreRelativo2
    er2 = ea2/vm2

    #SommaErroriRelativi
    ser = er1+er2

    #ErroreAssolutoFinale
    eaf = ser*pvm

    # restituisco i risultati
    print("il valore medio è: ) , pvm)
    print("l'errore assoluto è:" , eaf)

errore()
    

