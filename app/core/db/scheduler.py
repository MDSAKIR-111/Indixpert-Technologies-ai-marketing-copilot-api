"""
app/core/scheduler.py

Background job jo har 1 minute mein check karta hai:
kaunse content_calendar posts ka scheduled time aa gaya hai,
aur unhe automatically publish kar deta hai.
"""

import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.core.db.session import AsyncSessionLocal
from app.core.db.base_service import SPService
from app.modules.publisher.service import PublisherService

logger = logging.getLogger("auto_publish_scheduler")

scheduler = AsyncIOScheduler()


async def publish_due_content():
    """
    Due posts dhoondta hai aur ek-ek karke publish karta hai.
    Har item ke liye alag session use karta hai, taaki agar ek
    fail ho jaye toh baaki items par asar na pade.
    """

    async with AsyncSessionLocal() as session:
        try:
            due_items = await SPService.many(
                session=session,
                procedure_name="sp_get_due_content_calendar",
            )
        except Exception as e:
            logger.error(f"Failed to fetch due content calendar items: {e}")
            return

    if not due_items:
        return

    logger.info(f"[auto-publish] {len(due_items)} due post(s) found.")

    for item in due_items:
        async with AsyncSessionLocal() as session:
            try:
                await PublisherService.publish(
                    session=session,
                    workspace_id=item["workspace_id"],
                    calendar_id=item["id"],
                )
                logger.info(f"[auto-publish] Published calendar item {item['id']}")

            except Exception as e:
                logger.error(f"[auto-publish] Failed to publish {item['id']}: {e}")


def start_scheduler():
    scheduler.add_job(
        publish_due_content,
        trigger="interval",
        minutes=1,
        id="auto_publish_job",
        replace_existing=True,
    )
    scheduler.start()
    logger.info("Auto-publish scheduler started (runs every 1 minute).")


def stop_scheduler():
    scheduler.shutdown(wait=False)
    logger.info("Auto-publish scheduler stopped.")