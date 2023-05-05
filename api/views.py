from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from restaurant.models import Restaurant
from employee.models import Employee
from menu.models import Menu
from .serializers import RestaurantsSerializer, EmployeeSerializer, MenuSerializer


@api_view(['GET'])
def getRestaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantsSerializer(restaurants, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addRestaurants(request):
    serializer = RestaurantsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateRestaurants(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantsSerializer(instance=restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteRestaurants(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    restaurant.delete()
    return Response('Restaurant successfully deleted!')

#########################################################
@api_view(['GET'])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addEmployees(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateEmployees(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#########################################################
@api_view(['GET'])
def getMenu(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addMenu(request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    serializer = MenuSerializer(instance=menu, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
