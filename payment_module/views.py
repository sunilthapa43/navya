import base64
import hashlib
import hmac
import os

# from OpenSSL.crypto import (
#     load_pkcs12,
#     sign,
# )
from django.views.generic import TemplateView

CONNECT_IPS_PFX_FILE_PASSWORD = os.getenv("CONNECT_IPS_PFX_FILE_PASSWORD")
CONNECT_IPS_MERCHANT_ID = os.getenv("CONNECT_IPS_MERCHANT_ID")
CONNECT_IPS_USER_NAME = os.getenv("CONNECT_IPS_USER_NAME")
CONNECT_IPS_KEY_FILE = os.getenv("CONNECT_IPS_KEY_FILE")
CONNECT_IPS_APP_NAME = os.getenv("CONNECT_IPS_APP_NAME")

#
# message = "total_amount=120,transaction_uuid=11-205,product_code=EPAYTEST123"
#
# hmac_sha256 = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
# digest = hmac_sha256.digest()
# signature = base64.b64encode(digest).decode('utf-8')
# print(signature)


class EsewaPaymentTestView(TemplateView):
    template_name = "payment_module/esewa_test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        secret = "8gBm/:&EnhH.1/q"
        message = "total_amount=120,transaction_uuid=11-205,product_code=EPAYTEST123"
        hmac_sha256 = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
        digest = hmac_sha256.digest()
        signature = base64.b64encode(digest).decode("utf-8")
        body_data = {
            "amount": 1000,
            "failure_url": "https://www.youtube.com/",
            "product_delivery_charge": "0",
            "product_service_charge": "0",
            "product_code": "EPAYTEST123",
            "signature": signature,
            "signed_field_names": "total_amount,transaction_uuid,product_code",
            "success_url": "https://www.navyaadvisors.com/",
            "tax_amount": 0,
            "total_amount": 100,
            "transaction_uuid": "11-201-13",
        }
        context["body_data"] = body_data
        context["esewa_url"] = (
            "https://rc-epay.esewa.com.np/api/epay/login?bookingId=" + signature
        )
        return context


# def generate_token(txn_id, txn_date, txn_amount, ref_id, remarks, particulars):
#     with open(CONNECT_IPS_KEY_FILE, "rb") as f:
#         private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(f.read(), CONNECT_IPS_PFX_FILE_PASSWORD.encode())
#
#     message = (
#         "MERCHANTID="
#         + CONNECT_IPS_MERCHANT_ID
#         + ",APPID="
#         + CONNECT_IPS_USER_NAME
#         + ",APPNAME="
#         + CONNECT_IPS_APP_NAME
#         + ",TXNID="
#         + str(txn_id)
#         + ",TXNDATE="
#         + str(txn_date)
#         + ",TXNCRNCY="
#         + "NPR"
#         + ",TXNAMT="
#         + str(txn_amount)
#         + ",REFERENCEID="
#         + str(ref_id)
#         + ",REMARKS="
#         + str(remarks)
#         + ",PARTICULARS="
#         + str(particulars)
#         + ",TOKEN=TOKEN"
#     )
#     # sign the message
#     # signature = sign(key, message, "sha256")
#     signature = private_key.sign(
#         message.encode(),
#         padding.PKCS1v15(),
#         hashes.SHA256()
#     )
#     result = base64.b64encode(signature).decode()
#     return result
#
# print(generate_token(1, "2021-09-01", 100, 1, "remarks", "particulars"))


# def generate_token_for_validation(txn_id, txn_amt):
#     p12 = load_pkcs12(
#         open(CONNECTIPS_KEY_FILE, "rb").read(), CONNECT_IPS_PFX_FILE_PASSWORD.encode()
#     )
#     key = p12.get_privatekey()
#     message = (
#         "MERCHANTID="
#         + CONNECT_IPS_MERCHANT_ID
#         + ",APPID="
#         + CONNECT_IPS_USER_NAME
#         + ",REFERENCEID="
#         + str(txn_id)
#         + ",TXNAMT="
#         + str(txn_amt)
#     )
#     signature = sign(key, message, "sha256")
#     result = base64.b64encode(signature).decode()
#     payload = {
#         "merchantId": CONNECT_IPS_MERCHANT_ID,
#         "appId": CONNECT_IPS_USER_NAME,
#         "referenceId": txn_id,
#         "txnAmt": str(txn_amt),
#         "token": result,
#     }
#     return payload
#
#
# class InitiateBookACallPayment(IDNAPIView):
#     serializer_class = BookACallPaymentStatusSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         pid = uuid.uuid4().hex[:20]
#         ref_id = generate_random_code()
#         txn_date_ = timezone.now().date()
#         txn_date = txn_date_.strftime("%d-%m-%Y")
#         particulars = f"PAR-{ref_id}"
#         token = None
#         su = None
#         fu = BACKEND_URL + resolve_url("subscription-failure")
#         advisor_call = serializer.validated_data["advisor_call"]
#         total_amount = advisor_call.duration.price
#         khalti_initiate = None
#         amt_in_paisa = int(total_amount * 100)
#         payment_method = serializer.validated_data["payment_method"]
#         initiate_through = serializer.validated_data["initiate_through"]
#         remarks = f"Book A call Payment initiated by {advisor_call.full_name}"
#         if payment_method == "Khalti":
#             su = BACKEND_URL + "/vriddhi/api/v2/verify-khalti/"
#             payload = {
#                 "return_url": su,
#                 "website_url": "https://moneymitra.com",
#                 "amount": amt_in_paisa,
#                 "purchase_order_id": pid,
#                 "purchase_order_name": advisor_call.expertise.expertise,
#                 "customer_info": {
#                     "name": advisor_call.full_name,
#                     "email": advisor_call.email,
#                     "mobile": advisor_call.phone,
#                 },
#             }
#             KHALTI_REQUEST_URL = KHALTI_PAYMENT_BASE_URL + "epayment/initiate/"
#             headers = {
#                 "Authorization": f"Key {KHALTI_AUTH_KEY}",
#                 "Content-Type": "application/json",
#             }
#             response = requests.request("POST", KHALTI_REQUEST_URL, headers=headers, data=json.dumps(payload))
#             if response.status_code == 200:
#                 khalti_initiate = response.json()
#                 pid = khalti_initiate.get("pidx")
#             else:
#                 khalti_initiate = "Khalti payment initiation failed"
#
#         elif payment_method == "Esewa":
#             su = BACKEND_URL + "/vriddhi/api/v2/verify-esewa/"
#
#         elif payment_method == "ConnectIPS":
#             su = BACKEND_URL + "/vriddhi/api/v2/verify-connect-ips/"
#
#             token = generate_token(
#                 txn_id=pid,
#                 txn_date=txn_date,
#                 txn_amount=amt_in_paisa,
#                 ref_id=ref_id,
#                 remarks=remarks,
#                 particulars=particulars,
#             )
#
#         BookACallPaymentStatus.objects.create(
#             advisor_call=advisor_call,
#             user=self.request.user,
#             payment_method=payment_method,
#             product_id=pid,
#             ref_id=ref_id,
#             payment_date=txn_date_,
#             initiate_through=initiate_through,
#             paid_amount=total_amount,
#             status="Pending",
#         )
#
#         return SuccessResponse(
#             data={
#                 "txn_id": pid,
#                 "token": token,
#                 "su": su,
#                 "fu": fu,
#                 "txn_date": txn_date,
#                 "total_amount": total_amount,
#                 "total_amount_in_paisa": amt_in_paisa,
#                 "remarks": remarks,
#                 "particulars": particulars,
#                 "ref_id": ref_id,
#                 # for esewa specific
#                 "esewa_initiate_url": ESEWA_INITIATE_URL,
#                 #     for connect ips specific
#                 "connect_ips_user_name": CONNECT_IPS_USER_NAME,
#                 "connect_ips_app_name": CONNECT_IPS_APP_NAME,
#                 "connect_ips_merchant_id": CONNECT_IPS_MERCHANT_ID,
#                 "connect_ips_initiate_url": CONNECTIPS_INITIATE_URL,
#                 #     for khalti specific
#                 "khalti_initiate": khalti_initiate,
#                 "after_success_url": su,
#                 "after_failure_url": fu,
#             }
#         )
#
#
# class BookACallVerifyEsewaPaymentAPIView(View):
#     def get(self, request, *args, **kwargs):
#         esewa_refid = request.GET.get("refId")
#         esewa_oid = request.GET.get("oid")
#         amount = request.GET.get("amt")
#         payment_status = BookACallPaymentStatus.objects.filter(product_id=esewa_oid)
#
#         if payment_status.exists():
#             payment_status = payment_status.first()
#             data = {
#                 "amt": amount,
#                 "scd": ESEWA_SCD,
#                 "rid": esewa_refid,
#                 "pid": esewa_oid,
#             }
#             resp = requests.post(url=ESEWA_PAYMENT_VERIFICATION_URL, data=data)
#             if "Success" in resp.text:
#                 payment_status.status = "Completed"
#                 payment_status.save()
#                 with transaction.atomic():
#                     complete_book_a_call_payment(
#                         advisor_call=payment_status.advisor_call,
#                         user=payment_status.user,
#                         payment_via="Esewa",
#                         amount=payment_status.paid_amount,
#                         payment_verified=True,
#                     )
#                 return redirect("bool-a-call-payment-success")
#             else:
#                 payment_status.status = "Failed"
#                 payment_status.save()
#                 return redirect("mobile-subscription-failure")
#
#         return redirect("src:dashboard")
#
#
# class BookACallVerifyKhaltiPaymentAPIView(View):
#     def get(self, request, *args, **kwargs):
#         response = request.GET
#         pidx = response.get("pidx")
#         amount = response.get("amount")
#         # convert to rs
#         amount = float(amount) / 100
#         payment_status = BookACallPaymentStatus.objects.filter(product_id=pidx).first()
#         if pidx:
#             request_url = KHALTI_PAYMENT_BASE_URL + "epayment/lookup/"
#             data = {
#                 "pidx": str(pidx),
#             }
#             headers = {
#                 "Authorization": f"Key {KHALTI_AUTH_KEY}",
#                 "Content-Type": "application/json",
#             }
#             resp = requests.post(request_url, headers=headers, data=json.dumps(data))
#             status_code = resp.status_code
#             response = resp.json()
#             if status_code == 200 and response.get("status") == "Completed":
#                 with transaction.atomic():
#                     complete_book_a_call_payment(
#                         advisor_call=payment_status.advisor_call,
#                         user=payment_status.user,
#                         payment_via="Khalti",
#                         amount=amount,
#                         payment_verified=True,
#                     )
#                 payment_status.status = "Completed"
#                 payment_status.save()
#                 return redirect("bool-a-call-payment-success")
#             else:
#                 payment_status.status = "Failed"
#                 payment_status.save()
#                 return redirect("mobile-subscription-failure")
#
#         return redirect("src:dashboard")
#
#
# class BookACallVerifyConnectIPSPaymentAPIView(View):
#     def get(self, request, *args, **kwargs):
#         request_ = request.GET
#         txn_id = request_.get("TXNID")
#         payment_status = BookACallPaymentStatus.objects.filter(product_id=txn_id)
#         if payment_status.exists():
#             payment_status = payment_status.first()
#             amount = payment_status.paid_amount
#             url = settings.CONNECTIPS_VERIFY_URL
#             payload = generate_token_for_validation(txn_id=txn_id, txn_amt=amount)
#             headers = {
#                 "Content-Type": "application/json",
#             }
#             response = requests.post(
#                 url,
#                 data=json.dumps(payload),
#                 auth=HTTPBasicAuth(CONNECT_IPS_USER_NAME, CONNECT_IPS_PASSWORD),
#                 headers=headers,
#             )
#             if response.json().get("status") == "SUCCESS":
#                 with transaction.atomic():
#                     complete_book_a_call_payment(
#                         advisor_call=payment_status.advisor_call,
#                         user=payment_status.user,
#                         payment_via="ConnectIPS",
#                         amount=amount,
#                         payment_verified=True,
#                     )
#                 payment_status.status = "Completed"
#                 payment_status.save()
#                 return redirect("bool-a-call-payment-success")
#             else:
#                 payment_status.status = "Failed"
#                 payment_status.save()
#                 return redirect("mobile-subscription-failure")
#
#         return redirect("src:dashboard")
