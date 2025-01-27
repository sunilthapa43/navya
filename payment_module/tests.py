# import base64
# import hashlib
# import hmac
# import webbrowser
# from decimal import Decimal
#
# secret = "8gBm/:&EnhH.1/q"
#
# message = "total_amount=120,transaction_uuid=11-205,product_code=EPAYTEST123"
#
# hmac_sha256 = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
# digest = hmac_sha256.digest()
# signature = base64.b64encode(digest).decode('utf-8')
# print(signature)
#
# # open web view: https://rc-epay.esewa.com.np/api/epay/login?bookingId=sfz3vEeozivkVSD6C/kaTZLBYx8XDmEL+9zkmRm1MmU=, with post request
#
# def test_esewa():
#     # open web view
#     page = "https://rc-epay.esewa.com.np/api/epay/"
#     booking_id = "sfz3vEeozivkVSD6C/kaTZLBYx8XDmEL+9zkmRm1MmU="
#     url = f"{page}login?bookingId={booking_id}"
#
#     body = {
#         "amount": 90,
#         "failure_url": "https://www.youtube.com/",
#         "product_delivery_charge": "0",
#         "product_service_charge": "0",
#         "product_code": "EPAYTEST123",
#         "signature": "sfz3vEeozivkVSD6C/kaTZLBYx8XDmEL+9zkmRm1MmU=",
#         "signed_field_names": "total_amount,transaction_uuid,product_code",
#         "success_url": "https://www.navyaadvisors.com/",
#         "tax_amount": 0,
#         "total_amount": 100,
#         "transaction_uuid": "11-201-13"
#     }
#
#
# # test_esewa()
#
# def decode_response(encoded_message):
#     decoded_message = base64.b64decode(encoded_message).decode('utf-8')
#     # convert the string to dictionary
#     decoded_message = eval(decoded_message)
#     print(decoded_message)
#     print(decoded_message['status'])
#     print(decoded_message['transaction_code'])
#     print(decoded_message['total_amount'])
#
# decode_response("eyJ0cmFuc2FjdGlvbl9jb2RlIjoiMExENUNFSCIsInN0YXR1cyI6IkNPTVBMRVRFIiwidG90YWxfYW1vdW50IjoiMSwwMDAuMCIsInRyYW5zYWN0aW9uX3V1aWQiOiIyNDA2MTMtMTM0MjMxIiwicHJvZHVjdF9jb2RlIjoiTlAtRVMtQUJISVNIRUstRVBBWSIsInNpZ25lZF9maWVsZF9uYW1lcyI6InRyYW5zYWN0aW9uX2NvZGUsc3RhdHVzLHRvdGFsX2Ftb3VudCx0cmFuc2FjdGlvbl91dWlkLHByb2R1Y3RfY29kZSxzaWduZWRfZmllbGRfbmFtZXMiLCJzaWduYXR1cmUiOiJNcHd5MFRGbEhxcEpqRlVER2ljKzIybWRvZW5JVFQrQ2N6MUxDNjFxTUFjPSJ9")


"""
For esewa: message to be signed contains total_amount, transaction_uuid, product_code compulsory fields
For CIPS: message to be signed : MERCHANTID=550,APPID=MER-550-APP-1,REFERENCEID=txn-123,TXNAMT=500

"""

# grpc client to test the connection

import grpc

from payment_module.protos import account_pb2, account_pb2_grpc

with grpc.insecure_channel("localhost:50051") as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)
    response = stub.List(account_pb2.UserListRequest())
    for res in response:
        print(res)
    user = stub.Retrieve(account_pb2.UserRetrieveRequest(id=1))
    print("USER IS: ", user)
    print("Type of user is: ", type(user))
