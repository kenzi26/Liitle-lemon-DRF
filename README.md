## A FULLY FUNCTIONAL BACKEND SIDE OF A CLIENT-BASED RESTAURANT WEBSITE USING DJANGO REST FRAMEWORK(DRF) ##

This project is called Little-LemonDRF, it basically demonstrate how the backend side of liitle-Lemon restaurant website can be built using Django Rest Framework(DRF). The backend design using DRF was fully done by myself. Every part of this project shows the following fuctionalities below.

## BENIFITS OF USING DRF FOR LITTLE-LEMON WEBSITE ##
Django rest framework(DRF) is a powerful tool for building web APIs. DRF makes it easy to create APIs which complex functionalities. Having applied the backend design with DRF. it provides the following benifits to Little-Lemon:

* Little-Lemon with the right code was able to make use of Django adminstration which provided admin with certain important authorization to add menu-items, change and modify prices of menu-items.

* Creation Of tokens for permission into important part of Little-Lemon website.

* Throttle check for misusing for the APIs are configured at the app level and Its set to 10times per call.

* Serialization on the app level consist of id, title, price, stock and price_after_tax all these are configured and can be accessed use the Browersable API endpoint after configuring the url pattern. It is used for add menu-items.

* Using Insomnia for creating a (GET, POST, PUT) request to regenrate token, blacklist a token, encrypt a message although alternatively the browserable APIs also provides this function.

* setting.py on the project level of the backend has the 'rest_framework' , 'djoser' , 'rest_frramework_simplejwt' just to name a few was used to configure the brosweable API, token creation for effective performance to the website.

* sqlite is the database management system used for storing of data.

* IsAuthenticated was imported from rest framework for encryption of data from unauthorized users.


# AIMS AND OBJECTIVES OF USING DRF FOR LITTLE-LEMON WEBSITE #
DRF provided an architectural style for designing APIs used in Little-Lemon website. DRF was very effective in providing admin priviledges such as adding of menu items, token access for security, broswerable API, filter and searching of menu items and so many more.


# PROJECT BY: MOKWENYE KENECHUKWU KELAN #
