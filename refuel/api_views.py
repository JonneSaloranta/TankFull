# # TODO: Add authentication to API views and make sure they work

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_vehicles(request, user_id):
#     user = get_object_or_404(get_user_model(), id=user_id)
#     vehicles = Vehicle.objects.filter(user=user)
#     serialized_vehicles = VehicleSerializer(vehicles, many=True).data
#     return Response({'user': UserSerializer(instance=user).data, 'vehicles': serialized_vehicles}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def create_vehicle(request):
#     vehicleform = VehicleForm(request.data)

#     if vehicleform.is_valid():
        # user = models.ForeignKey(User, on_delete=models.CASCADE)
        # vehicle_name = models.CharField(max_length=100)
        # make = models.CharField(max_length=100, null=True, blank=True)
        # model = models.CharField(max_length=100, null=True, blank=True)
        # year = models.IntegerField(null=True, blank=True)
        # fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)

    #     user = get_object_or_404(get_user_model(), id=request.data.get('user_id'))
    #     vehicle_name = request.data.get('vehicle_name')
    #     make = request.data.get('make')
    #     model = request.data.get('model')
    #     year = request.data.get('year')
    #     fuel_type = get_object_or_404(FuelType, fuel_type=request.data.get('fuel_type'))

    #     vehicle = Vehicle.objects.create(user=user, vehicle_name=vehicle_name, make=make, model=model, year=year, fuel_type=fuel_type)
    #     serialized_vehicle = VehicleSerializer(vehicle).data
    #     return Response({'user': UserSerializer(instance=user).data, 'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)        
    # else:
    #     return Response({'message': 'Invalid vehicle form'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_vehicle(request):
#     vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
#     vehicle.delete()
#     return Response({'message': 'Vehicle deleted successfully'}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def create_refuel(request):
#     user = get_object_or_404(get_user_model(), id=request.data.get('user_id'))
#     vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
#     refuel = Refuel.objects.create(user=user, vehicle=vehicle, odometer=request.data.get('odometer'), fuel_amount=request.data.get('fuel_amount'), cost=request.data.get('cost'))
#     serialized_refuel = RefuelSerializer(refuel).data
#     return Response({'user': UserSerializer(instance=user).data, 'vehicle': VehicleSerializer(instance=vehicle).data, 'refuel': serialized_refuel}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_refuel(request):
#     refuel = get_object_or_404(Refuel, id=request.data.get('refuel_id'))
#     refuel.delete()
#     return Response({'message': 'Refuel deleted successfully'}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def update_refuel(request):
#     refuel = get_object_or_404(Refuel, id=request.data.get('refuel_id'))
#     refuel.odometer = request.data.get('odometer')
#     refuel.fuel_amount = request.data.get('fuel_amount')
#     refuel.cost = request.data.get('cost')
#     refuel.save()
#     serialized_refuel = RefuelSerializer(refuel).data
#     return Response({'refuel': serialized_refuel}, status=status.HTTP_200_OK)

# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def update_vehicle(request):
#     vehicle = get_object_or_404(Vehicle, id=request.data.get('vehicle_id'))
#     vehicle.vehicle_name = request.data.get('vehicle_name')
#     vehicle.save()
#     serialized_vehicle = VehicleSerializer(vehicle).data
#     return Response({'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_refuels(request, user_id):
#     user = get_object_or_404(get_user_model(), id=user_id)
#     refuels = Refuel.objects.filter(user=user)
#     serialized_refuels = RefuelSerializer(refuels, many=True).data
#     return Response({'user': UserSerializer(instance=user).data, 'refuels': serialized_refuels}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def vehicle_refuels(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#     refuels = Refuel.objects.filter(vehicle=vehicle)
#     serialized_refuels = RefuelSerializer(refuels, many=True).data
#     return Response({'vehicle': VehicleSerializer(instance=vehicle).data, 'refuels': serialized_refuels}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def refuel_details(request, refuel_id):
#     refuel = get_object_or_404(Refuel, id=refuel_id)
#     serialized_refuel = RefuelSerializer(refuel).data
#     return Response({'refuel': serialized_refuel}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def vehicle_details(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#     serialized_vehicle = VehicleSerializer(vehicle).data
#     return Response({'vehicle': serialized_vehicle}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_details(request, user_id):
#     user = get_object_or_404(get_user_model(), id=user_id)
#     serialized_user = UserSerializer(user).data
#     return Response({'user': serialized_user}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def get_fuel_types(request):
#     fuel_types = FuelType.objects.all()
#     serialized_fuel_types = FuelTypeSerializer(fuel_types, many=True).data
#     return Response({'fuel_types': serialized_fuel_types}, status=status.HTTP_200_OK)