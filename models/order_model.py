from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from utils.customHandlers import CustomObjectId
from models.review_model import Review

class ProcessStatus(str, Enum):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

class Invoice(BaseModel):
    invoice_url: str
    invoice_id: str


class Order(BaseModel):
    product_id: CustomObjectId
    product_name: str

    transaction_id: CustomObjectId
    transaction_status: ProcessStatus

    delivry_id: CustomObjectId
    delivery_status: ProcessStatus
    
    order_rating: Review | None
    quantity : int = 0
    dateCreated: datetime


class Delivery(BaseModel):
    order_id: CustomObjectId

    address: str
    phone_number: int
    
    delivery_status: ProcessStatus    
    delivery_feedback: str | None
    deliveryTimeStamp: datetime | None


class Transaction(BaseModel):
    order_id: CustomObjectId

    transaction_num: str # This is different than transaction id. this will be provided by the payment gateways(stripe, paypal, etc)
    transaction_status: ProcessStatus
    transaction_failed_reason: str | None

    product_price: float
    delivery_charge: float
    discount: float
    invoice: Invoice


class Refund(BaseModel):
    order_id: CustomObjectId
    transaction_id: CustomObjectId
    
    refund_status: ProcessStatus
    refund_reason: str
    refund_amount: float
    refund_transaction_num: str
    refund_invoice: Invoice
