from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import bot

async def go_do_test(bot: Bot):
        await bot.send_message(1045935241, "Иди делай русский!")

async def wake_up(bot: Bot):
        video = open("image/video.mp4", "rb")
        await bot.send_video(1045935241, video=video)


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        go_do_test,
        trigger=CronTrigger(day_of_week=3, hour=20, minute=30),
        kwargs={"bot": bot}
    )
    scheduler.add_job(
        wake_up,
        trigger=CronTrigger(day_of_week=3, hour=20, minute=30),
        kwargs={"bot": bot}
    )
    scheduler.start()