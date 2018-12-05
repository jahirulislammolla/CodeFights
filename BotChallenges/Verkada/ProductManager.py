class ProductManager:
    products = []
    def createProduct(self, id, title):
        # TODO: return false if the product id already exists
        product = {}
        product['id'] = id
        product['title'] = title
        if product in self.products:
            return False
        self.products.append(product)
        return True

    def updateProduct(self, id, title):
        # TODO: return false if the product id does not exist
        ck=0
        updproduct = {}
        for product in self.products:
            if product['id'] == id:
                updproduct = product
                ck=1
        if ck==0:
            return False
        updproduct['title'] = title
        return True

    def deleteProduct(self, id):
        # TODO: return false if the product does not exist

        updproduct = {}
        ck=0
        for product in self.products:
            if product['id'] == id:
                updproduct = product
                ck=1
        if ck==0:
            return False
        del updproduct
        return True

    def findProductById(self, id):
        # product or null
        for product in self.products:
            if product['id'] == id:
                return product
        return None

    def findProductByTitle(self, title):
        # product or null
        for product in self.products:
            if product['title'] == title:
                return product
        return None

productManager = ProductManager()

import json
from collections import OrderedDict
def productManagement(operations):
    # Calls corresponding methods of productManager based on the input
    ans = []
    for operation in operations:
        if operation[0] == 'createProduct':
            res = productManager.createProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'updateProduct':
            res = productManager.updateProduct(operation[1], operation[2])
            ans.append(json.dumps(res))
        if operation[0] == 'deleteProduct':
            res = productManager.deleteProduct(operation[1])
            ans.append(json.dumps(res))
        if operation[0] == 'findProductById':
            res = productManager.findProductById(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(OrderedDict(res), separators=(',', ':')))
        if operation[0] == 'findProductByTitle':
            res = productManager.findProductByTitle(operation[1])
            if res == None:
                ans.append('null')
            else:
                ans.append(json.dumps(OrderedDict(res), separators=(',', ':')))
    return ans
