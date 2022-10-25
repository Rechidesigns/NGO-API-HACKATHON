from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from account.permissions import IsAdminOrReadOnly
from .models import Blog, Ngo
from .serializers import BlogSerializer
from .serializers import NgoSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication

 
class NgoView(APIView):
    """
    Retrive all or create new Ngos instances
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request, format=None):
        """ Use this method to get all Ngo instances"""

        objs = Ngo.objects.all() #get data
        serializers = NgoSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=NgoSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = NgoSerializer(data=request.data)
            #get the data and deserialization

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        

class NgoDetailView(APIView):
    """
    Retrive, update or delete a Ngo instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, ngo_id):
        """"Get a single instance using the provided ngo_id""" 

        try:
            return Ngo.objects.get(id=ngo_id)
        except Ngo.DoesNotExist:
            raise NotFound(detail = {"message", "Ngo not found"})
        
    def get(self, request, ngo_id, format=None):
        obj = self.get_object(ngo_id)
        serializer = NgoSerializer(obj)

        data = {
            "message" :"success"
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(method="put", request_body=NgoSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, ngo_id, format=None):
        obj = self.get_object(ngo_id)
        serializer = NgoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message" :"success"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message" :"failed",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, ngo_id, formart=None):
        obj = self.get_object(ngo_id)
        if obj.Ngo.count() == 0:

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this Ngo because it contains real NGOs."})



class BlogView(APIView):

    """
    Retrive all or create new Blog instances.
    """
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    
    def get(self, request, format=None):

        objs = Blog.objects.all() #get data
        serializers = BlogSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="post", request_body=BlogSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = BlogSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                data = {
                    "message" :"success"
                    }               
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                data = {
                    "message" :"failed",
                    "error" : serializer.error
                }

                return Response(data, status=status.HTTP_400_BAD_REQUEST)



    
class BlogDetailView(APIView):
    """
    Retrieve, update or delete a Blog instance
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]
    
    def get_object(self, blog_id):
        """Get a single blog instance using the provided blog_id"""
        try:
            return Blog.objects.get(id = blog_id)
        except Ngo.DoesNotExist:
            raise NotFound(detail = {"message": "Item not found"})
        
    def get(self, request, blog_id, format=None):
        obj = self.get_object(blog_id)
        serializer = BlogSerializer(obj)
        
        data = {
            "message":"success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=BlogSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, blog_id, format=None):
        obj = self.get_object(blog_id)
        serializer = BlogSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            data ={
                    "message" : "success",   
            }
            return Response(data, status=status.HTTP_201_CREATED)
          
        else:
            data ={
                    "message" : "Failed", 
                    "error": serializer.errors 
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)   
    def delete(self, request, blog_id, format=None):
        obj = self.get_object(blog_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)