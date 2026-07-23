from src.database import Database

db = Database()

engine = db.connect()

print(engine)






















''''
python -m tests.test.py                                                                
python -m tests.test_database.py                                                       
python -m tests.test_extract.py                                                        
python -m tests.test_load_customer.py                                                  
python -m tests.test_load_date.py                                                      
python -m tests.test_load_fact.py                                                      
python -m tests.test_load_product.py                                                   
python -m tests.test_load_region.py                                                    
python -m tests.test_scd.py                                                            
python -m tests.test_transform.py                                                      

'''                                                          
