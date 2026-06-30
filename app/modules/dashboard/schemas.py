from datetime import datetime
from pydantic import BaseModel


class DashboardOverview(BaseModel):
    total_brands: int
    total_generated_content: int
    total_scheduled_posts: int
    total_published_posts: int
    total_failed_posts: int
    connected_social_accounts: int
    estimated_ai_cost: float
    total_followers: int
    total_likes: int
    total_comments: int
    total_shares: int


class RecentActivity(BaseModel):
    activity_type: str
    title: str
    platform: str
    status: str
    activity_time: datetime