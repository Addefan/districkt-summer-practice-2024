from sqlalchemy import Integer, String, DateTime, ForeignKey, JSON, Interval
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, autoincrement=False)

    name = mapped_column(String(255))
    second_name = mapped_column(String(255))

    email = mapped_column(String(254))


class AttendanceStatistic(Base):
    __tablename__ = "attendance_statistics"
    id = mapped_column(Integer, primary_key=True)

    new = mapped_column(Integer)
    other = mapped_column(Integer)
    regular = mapped_column(Integer)


class PlatformStatistic(Base):
    __tablename__ = "platform_statistics"
    id = mapped_column(Integer, primary_key=True)

    android = mapped_column(Integer)
    web = mapped_column(Integer)
    ios = mapped_column(Integer)


class Event(Base):
    __tablename__ = "events"
    id = mapped_column(Integer, primary_key=True, autoincrement=False)

    name = mapped_column(String)

    starts_at = mapped_column(DateTime)
    ends_at = mapped_column(DateTime)
    duration = mapped_column(Interval)

    invited_count = mapped_column(Integer)
    invited_visited_count = mapped_column(Integer)

    registered_count = mapped_column(Integer)
    registered_visited_count = mapped_column(Integer)

    attendance_id = mapped_column(Integer, ForeignKey("attendance_statistics.id"))
    attendance = relationship(AttendanceStatistic, uselist=False)

    country = mapped_column(JSON)

    platform_id = mapped_column(Integer, ForeignKey("platform_statistics.id"))
    platform = relationship(PlatformStatistic, uselist=False)

    utms = mapped_column(JSON)

    create_user_id = mapped_column(Integer, ForeignKey("users.id"))
    create_user = relationship(User, back_populates="events")

    referrer = mapped_column(JSON)

    context = mapped_column(String(127))
