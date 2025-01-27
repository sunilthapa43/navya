from django.db import models


class Merchant(models.Model):
    class MerchantChoices(models.TextChoices):
        ESEWA = "ESEWA", "Esewa"
        KHALTI = "KHALTI", "Khalti"
        CONNECTIPS = "CONNECTIPS", "ConnectIPS"
        IMEPAY = "IMEPAY", "IME Pay"

    # for merchant code, which might be changed or added in future
    code = models.TextField(
        max_length=20, verbose_name="Merchant Code", blank=False, null=False
    )
    name = models.TextField(
        max_length=20,
        verbose_name="Merchant Name",
        choices=MerchantChoices.choices,
        default=MerchantChoices.ESEWA,
        blank=False,
        null=False,
    )


# class for payment module


class Payment(models.Model):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        verbose_name="Merchant",
        blank=False,
        null=False,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Amount in Rs",
        blank=False,
        null=False,
    )
    transaction_id = models.TextField(
        max_length=50, verbose_name="Transaction ID", blank=False, null=False
    )


class PaymentStatus(models.Model):
    class PaymentStatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SUCCESS = "SUCCESS", "Success"
        FAILED = "FAILED", "Failed"
        CANCELLED = "CANCELLED", "Cancelled"

    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, verbose_name="Payment", blank=False, null=False
    )
    status = models.TextField(
        max_length=20,
        verbose_name="Payment Status",
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PENDING,
        blank=False,
        null=False,
    )
    response = models.TextField(
        max_length=500, verbose_name="Response", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
