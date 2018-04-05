from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# import comnig from django
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
# import coming from the drf



class Business(APIView) :
    """
    test of the home views
    """
    def get(self, request):
        return Response('hello')
    # authentication_classes = (CustomAuth, )
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    # def get( self, request, format=None ):
        # post = Post.objects.all()
        # serializer = PostSerializer( post , many=True)
        # return Response(serializer.data)
    
    # def post(self, request, format=None):
        # post = Post.objects.all()
        # serializer = PostSerializer( data=request.data )
        # if serializer.is_valid():

            # serializer.save(post_owner=self.request.user)
            # return Response(status.HTTP_201_CREATED)
        # return Response(status.HTTP_422_UNPROCESSABLE_ENTITY)


# class Home_Detail(APIView):
    # '''
    # I try the detailed view
    # '''
    # def get_post(self, id):
        
        # try:
            # return Post.objects.get(id=id)
        # except Post.DoesNotExist:
            # raise Http404
    # #ici j'ai d'abord fait un get_post pour etre sur de raise un flag si jamais indice n'existe pas
   

    # def get( self,  request, id):
        # post = self.get_post(id)
        # serializer = PostSerializer(post)
        # return Response(serializer.data)
    # # ici je fais un simple get ou je trouve les post que je veux prendre et je les ajoute et return 
    
    # def delete(self, request, id):
        # post = self.get_post(id)
        # post.delete()
        # return Response('post number '+ id + ' deleted ')
    

    # #here i used thhe partial to accept the patch method but you can fully change it if you want 
    # def put(self, request, id):
        # post = self.get_post(id)
        # serializer = PostSerializer(post, request.data, partial=True)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # return Response('not gonna happen')








# # Create your views here.


