"""
app/modules/social_publish/service.py

Platform ke hisaab se sahi publisher ko dispatch karta hai.
"""

from app.modules.social_publish.facebook import FacebookPublisher
from app.modules.social_publish.linkedin import LinkedInPublisher


class SocialPublishService:

    @staticmethod
    async def publish(
        platform: str,
        social_account: dict,
        generated_content: dict,
    ):

        platform = platform.lower()

        if platform == "facebook":

            return await FacebookPublisher.publish_text(
                page_id=social_account["page_id"],
                access_token=social_account["access_token"],
                message=generated_content["generated_text"],
            )

        if platform == "linkedin":

            return await LinkedInPublisher.publish_text(
                account_id=social_account["account_id"],
                access_token=social_account["access_token"],
                message=generated_content["generated_text"],
            )

        raise Exception(f"{platform} not supported.")