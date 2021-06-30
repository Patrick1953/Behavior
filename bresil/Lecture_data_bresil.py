# coding: utf-8
from Lecture_csv import Lecture_csv

class Lecture_data_bresil () :
    
    def __init__ (self, path = './') :
        
        self.path = path
        
        self.dico_csv = {
            'customer' : '../data_bresil/olist_customers_dataset.csv',
            'geolocation' : '../data_bresil/olist_geolocation_dataset.csv',
            'orders_items' : '../data_bresil/olist_order_items_dataset.csv',
            'order_payments' : '../data_bresil/olist_order_payments_dataset.csv',
            'order_reviews' : '../data_bresil/olist_order_reviews_dataset.csv',
            'orders' : '../data_bresil/olist_orders_dataset.csv',
            'products' : '../data_bresil/olist_products_dataset.csv',
            'sellers' : '../data_bresil/olist_sellers_dataset.csv',
            'product_category_name_translation' : '../data_bresil/product_category_name_translation.csv',
            }
        
        self.nombre_erreur = 0
        
    def get_dico (self, nameFile, nom_zone) :
        
        nameFile_reel = self.dico_csv [nameFile]
        
        L = Lecture_csv (self.path, nameFile_reel)
        dico = {}
        
        for row in L.read_iterator ():
            dico [row[nom_zone] ] = row
            continue
        return dico
    
    def add (self,
             dico,
             
             nom_lien1, dico1,
             nom_lien2, dico2,
             
             liste_ajout,
             row_erreur,
             is_del_bad_ID = False,
            
            ) :
        
        liste_bad_ID = []
        for ID, data_dico_final in dico.items() :
            
            isErreur = False
            try :
                valeur_lien = data_dico_final [nom_lien1]
                # la cle de dico1 == zone qui est lie à nom_lien1 dans  enreg dico (par ID customer)
                data_dico = dico1 [valeur_lien] 
            except:
                self.nombre_erreur += 1
                isErreur = True
                pass
        
                
            if isErreur and not nom_lien2 is None:
                try :
                    valeur_lien = data_dico_final [nom_lien2]
                    data_dico = dico1 [valeur_lien]
                except:
                    self.nombre_erreur += 1
                    if is_del_bad_ID :
                        liste_bad_ID.append (ID)
                        continue
                    
                    dico [ID] = row_erreur
                    
                    continue
                      
               
            for nom_zone in liste_ajout  :
                data = data_dico [nom_zone]
                data_dico_final [nom_zone] = data
                
                continue
            dico [ID] = data_dico_final
            continue
        for ID in liste_bad_ID :
            del dico [ID]
                
        return dico
    
    
    def join_consumer_geolocalization (self, ) :
        """
        on realise la jointure par la geolisation
        ou
        par le nom de ville (deuxieme choix)
                
        """
        
        nameFile = 'customer'
        nom_zone = 'customer_id'
        dico = self.get_dico (nameFile, nom_zone)
        
        nameFile = 'geolocation'
    
        nom_zone = 'geolocation_zip_code_prefix'
        dico1 = self.get_dico (nameFile, nom_zone)
        nom_lien1 = 'customer_zip_code_prefix'

        nom_zone = 'geolocation_city'
        dico2 = self.get_dico (nameFile, nom_zone)
        nom_lien2 = 'customer_city'


        liste_ajout = ['geolocation_lat', 'geolocation_lng',
                       'geolocation_state',
                      ]


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        
        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                  )
        
        return dico_resultat
    
    def join_customers_orders (self,dico_resultat) :
        
        nom_zone = 'customer_id'
        dico = dico_resultat 

        nameFile = 'orders'
        nom_zone = 'customer_id' # cle d' acces
        dico1 = self.get_dico (nameFile, nom_zone)
        nom_lien1 = 'customer_id'


        '''
        nom_zone = 'geolocation_city'
        dico2 = self.get_dico (nameFile, nom_zone)
        nom_lien2 = 'customer_city'
        '''
        nom_lien2 = None
        dico2 = {}



        liste_ajout = ['order_id',
                         'order_status',
                         'order_purchase_timestamp',
                         'order_approved_at',
                         'order_delivered_carrier_date',
                         'order_delivered_customer_date',
                         'order_estimated_delivery_date']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                         nom_lien1, dico1,
                                         nom_lien2, dico2,
                                         liste_ajout,
                                         row_erreur,
                                         is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    def join_customers_orders_items (self, dico_resultat) :
        
        dico = dico_resultat 
        nameFile = 'orders_items'

        nom_zone = 'order_id' # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)
        nom_lien1 = 'order_id' # valeur dans enreg dico


        '''
        nom_zone = 'geolocation_city'
        dico2 = self.get_dico (nameFile, nom_zone)
        nom_lien2 = 'customer_city'
        '''
        nom_lien2 = None
        dico2 = {}



        liste_ajout = [  'product_id',
                         'seller_id',
                         'shipping_limit_date',
                         'price',
                         'freight_value']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    def join_customers_products (self, dico_resultat):
        
        dico = dico_resultat 
        nameFile = 'products'

        nom_zone = 'product_id' 
        # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)
        nom_lien1 = 'product_id' # valeur dans enreg dico

        nom_lien2 = None
        dico2 = {}



        liste_ajout = [
                        'product_category_name',
                        'product_name_lenght',
                        'product_description_lenght',
                        'product_photos_qty',
                        'product_weight_g',
                        'product_length_cm',
                        'product_height_cm',
                        'product_width_cm']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    def join_customers_products_translation (self, dico_resultat):
        
        dico = dico_resultat 
        nameFile = 'product_category_name_translation'

        nom_zone = '\ufeffproduct_category_name'
        # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)

        nom_lien1 = 'product_category_name' # valeur dans enreg dico

        nom_lien2 = None
        dico2 = {}



        liste_ajout = [ 'product_category_name_english']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    def join_customers_sellers (self, dico_resultat):
        
        dico = dico_resultat 
        nameFile = 'sellers'

        nom_zone = 'seller_id'
        # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)
        
        nom_lien1 = 'seller_id' # valeur dans enreg dico

        nom_lien2 = None
        dico2 = {}



        liste_ajout = [ 'seller_city', 'seller_state']

        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    
    def join_customers_payments (self, dico_resultat):
        
        dico = dico_resultat 
        nameFile = 'order_payments'

        nom_zone = 'order_id'
        # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)

        nom_lien1 = 'order_id' # valeur dans enreg dico

        nom_lien2 = None
        dico2 = {}



        liste_ajout = [
                         'payment_sequential',
                         'payment_type',
                         'payment_installments',
                         'payment_value']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        return dico_resultat
    
    def join_customers_reviews (self, dico_resultat):
        
        dico = dico_resultat 
        nameFile = 'order_reviews'

        nom_zone = 'order_id'
        # cle d' acces du dico1
        dico1 = self.get_dico (nameFile, nom_zone)

        nom_lien1 = 'order_id' # valeur dans enreg dico

        nom_lien2 = None
        dico2 = {}



        liste_ajout = [
                         'review_score',
                         'review_comment_title',
                         'review_comment_message',
                         'review_creation_date',
                         'review_answer_timestamp']


        row_erreur = {}
        for nom_zone in liste_ajout :
            row_erreur [nom_zone] = ''

        dico_resultat  = self.add (  dico,
                                     nom_lien1, dico1,
                                     nom_lien2, dico2,
                                     liste_ajout,
                                     row_erreur,
                                     is_del_bad_ID = True,

                                      )
        
        
        return dico_resultat
    
    
    def dico_customers (self,) :
        
        
        nameFile = 'customer'
        nom_zone = 'customer_id'
        dico = self.get_dico (nameFile, nom_zone)

        


        dico_resultat  = self.join_consumer_geolocalization ()


        assert len (dico_resultat) == 99163


        dico_resultat  = self.join_customers_orders (dico_resultat)

        

        # customers orders_items


        dico_resultat = self.join_customers_orders_items (dico_resultat)

        

        # customers customer lien à product

        dico_resultat = self.join_customers_products ( dico_resultat)
        # customers customer lien à product_category_name (traduction english)
            

        dico_resultat  = self.join_customers_products_translation (dico_resultat)

        # consumers à sellers
        dico_resultat = self.join_customers_sellers ( dico_resultat)
        
        #  customer  payment

        dico_resultat = self.join_customers_payments (dico_resultat)

        # customer review
               
        dico_resultat = self.join_customers_reviews (dico_resultat)
                
        return dico_resultat
        
       
