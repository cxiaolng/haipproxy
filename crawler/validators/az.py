"""
We use this validator to filter ip that can access  amazon website.
"""
from config.settings import (
    TEMP_AZ_QUEUE, VALIDATED_AZ_QUEUE,
    TTL_AZ_QUEUE, SPEED_AZ_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class AmazonValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of az proxy resources"""
    name = 'az'
    urls = [
        'https://www.amazon.com'
    ]
    task_queue = TEMP_AZ_QUEUE
    score_queue = VALIDATED_AZ_QUEUE
    ttl_queue = TTL_AZ_QUEUE
    speed_queue = SPEED_AZ_QUEUE
    success_key = 'Amazon.com'
