from datetime import timedelta, datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, JSON, Interval
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)

    name: Mapped[str] = mapped_column(String(255))
    second_name: Mapped[str] = mapped_column(String(255))

    email: Mapped[str] = mapped_column(String(254))


class AttendanceStatistic(Base):
    __tablename__ = "attendance_statistics"
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"), primary_key=True)
    event: Mapped["Event"] = relationship("Event", back_populates="attendance_statistic")

    new: Mapped[int] = mapped_column(Integer)
    other: Mapped[int] = mapped_column(Integer)
    regular: Mapped[int] = mapped_column(Integer)


class PlatformStatistic(Base):
    __tablename__ = "platform_statistics"
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"), primary_key=True)
    event: Mapped["Event"] = relationship("Event", back_populates="platform_statistic")

    android: Mapped[int] = mapped_column(Integer)
    web: Mapped[int] = mapped_column(Integer)
    ios: Mapped[int] = mapped_column(Integer)


class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)

    name: Mapped[str] = mapped_column(String)

    starts_at: Mapped[datetime] = mapped_column(DateTime)
    ends_at: Mapped[datetime] = mapped_column(DateTime)
    duration: Mapped[timedelta] = mapped_column(Interval)

    invited_count: Mapped[int] = mapped_column(Integer)
    invited_visited_count: Mapped[int] = mapped_column(Integer)

    registered_count: Mapped[int] = mapped_column(Integer)
    registered_visited_count: Mapped[int] = mapped_column(Integer)

    attendance_statistic: Mapped[AttendanceStatistic] = relationship(AttendanceStatistic)

    country: Mapped[dict] = mapped_column(JSON)

    platform_statistic: Mapped[PlatformStatistic] = relationship(PlatformStatistic)

    utms: Mapped[dict] = mapped_column(JSON)

    create_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    create_user: Mapped[User] = relationship(User)

    referrer: Mapped[dict] = mapped_column(JSON)

    context: Mapped[str] = mapped_column(String(127))
