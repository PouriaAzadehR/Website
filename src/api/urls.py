from django.urls import include, path

from src.api.views.authentication import (
    RefreshToken,
    SendOneTimePassword,
    VerifyOneTimePassword,
)
from src.api.views.blog import (
    GetAboutUsNews,
    GetNewsBySlug,
    GetNewsList,
    SearchNews,
)
from src.api.views.categories import GetCategories
from src.api.views.events import (
    AddMember,
    CreateTeam,
    GetEventByID,
    GetEventList,
    GetEventRequirementsByEventID,
    GetTeam,
    GetTeamUser,
    Participation,
    RemoveMember,
    SearchEvents,
    SubmitRequirements,
    UpdateRequirements,
)
from src.api.views.facilities import (
    CancelReservation,
    CreateReservation,
    GetFacilityByID,
    GetFacilityList,
    GetFacilitySchedule,
    GetSessionSlots,
    SearchFacilities,
)
from src.api.views.notifications import (
    CreateNotifToken,
    GetNotificationBySlug,
    GetNotificationsList,
)
from src.api.views.oauth import Exchange
from src.api.views.oauth.oauth_login import OAuthLoginWeb
from src.api.views.polls import GetSurvey, SubmitAnswer
from src.api.views.profile import (
    AddEventToFavorite,
    AddTagToInterests,
    CreateNCRequest,
    GetFavoriteEvents,
    GetRegisteredEvents,
    GetTags,
    GetUserReservations,
    ProfileView,
    RemoveEventFromFavorite,
    RemoveTagFromInterests,
)
from src.api.views.storage import UploadFile
from src.api.views.website import (
    CreateTicket,
    GetAboutUs,
    GetFeaturedEvents,
    GetImportantNewsView,
)

authentication_urlpatterns = [
    path("otp/", SendOneTimePassword.as_view(), name="send-otp"),
    path("otp/verify/", VerifyOneTimePassword.as_view(), name="verify-otp"),
    path("otp/refresh/", RefreshToken.as_view(), name="refresh-token"),
]


oauth_urlpatterns = [
    path("sharif/login/", OAuthLoginWeb.as_view(), name="oauth-login"),
    path("", Exchange.as_view(), name="exchange"),
]

events_urlpatterns = [
    path("", GetEventList.as_view(), name="get_event_list"),
    path("search/", SearchEvents.as_view(), name="events"),
    path(
        "team/profile/<str:id>/", GetTeamUser.as_view(), name="get_team_user"
    ),
    path(
        "team/<str:team_id>/add/<str:sharif_id>/",
        AddMember.as_view(),
        name="add_team_member",
    ),
    path(
        "team/<str:team_id>/remove/<str:sharif_id>/",
        RemoveMember.as_view(),
        name="remove_team_member",
    ),
    path(
        "team/<str:team_id>/",
        GetTeam.as_view(),
        name="get_team",
    ),
    path("<str:id>/", GetEventByID.as_view(), name="get_event_by_id"),
    path("<str:id>/team/", CreateTeam.as_view(), name="create_team"),
    path(
        "participation/<str:event_id>/",
        Participation.as_view(),
        name="participation",
    ),
    path(
        "<str:event_id>/requirements/",
        GetEventRequirementsByEventID.as_view(),
        name="get_event_requirements_by_event_id",
    ),
    path(
        "<str:event_id>/submit_requirements/",
        SubmitRequirements().as_view(),
        name="submit_requirements",
    ),
    path(
        "<str:event_id>/update_requirements/",
        UpdateRequirements().as_view(),
        name="update_requirements",
    ),
]

facilities_urlpatterns = [
    path(
        "cancel_reservation/<str:id>/",
        CancelReservation.as_view(),
        name="cancel_reservation",
    ),
    path("", GetFacilityList.as_view(), name="get_facility_list"),
    path(
        "slots/<str:id>/",
        GetSessionSlots.as_view(),
        name="get_session_slots",
    ),
    path(
        "reservation/<str:id>/",
        CreateReservation.as_view(),
        name="create_reservation",
    ),
    path(
        "facility/<str:id>/",
        GetFacilityByID.as_view(),
        name="get_facility_by_id",
    ),
    path(
        "<str:id>/schedule/",
        GetFacilitySchedule.as_view(),
        name="get_facility_schedule",
    ),
    path("search/", SearchFacilities.as_view(), name="search_facilities"),
]

notifications_urlpatterns = [
    path(
        "",
        GetNotificationsList.as_view(),
        name="notifications_list",
    ),
    path(
        "<str:slug>/",
        GetNotificationBySlug.as_view(),
        name="notification_by_slug",
    ),
]

blog_urlpatterns = [
    path("", GetNewsList.as_view(), name="news_list"),
    path("about-us/", GetAboutUsNews().as_view(), name="about-us"),
    path("new/<str:slug>/", GetNewsBySlug.as_view(), name="news_by_slug"),
    path("search/", SearchNews.as_view(), name="search_news"),
]

website_urlpatterns = [
    path(
        "featured-events/",
        GetFeaturedEvents.as_view(),
        name="get_featured_events",
    ),
    path("contact-us/", CreateTicket.as_view(), name="contact_us"),
    path("about-us/", GetAboutUs.as_view(), name="about_us"),
    path(
        "important-news/",
        GetImportantNewsView.as_view(),
        name="important_news",
    ),
]

storage_urlpatterns = [
    path("upload/", UploadFile.as_view(), name="upload_media"),
]

profile_urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("nc-request/", CreateNCRequest.as_view(), name="create_nc"),
    path(
        "reservations/",
        GetUserReservations.as_view(),
        name="user_reservations",
    ),
    path(
        "registered-events/",
        GetRegisteredEvents.as_view(),
        name="registered_events",
    ),
    path(
        "favorite_events/", GetFavoriteEvents.as_view(), name="favorite_events"
    ),
    path(
        "favorite_events/add/<str:event_id>/",
        AddEventToFavorite.as_view(),
        name="add_event_to_favorite",
    ),
    path(
        "favorite_events/remove/<str:event_id>/",
        RemoveEventFromFavorite.as_view(),
        name="remove_event_from_favorite",
    ),
    path("interests/", GetTags.as_view(), name="interests"),
    path(
        "interests/add/<str:tag_id>/",
        AddTagToInterests.as_view(),
        name="add_tag_to_interest",
    ),
    path(
        "interests/remove/<str:tag_id>/",
        RemoveTagFromInterests.as_view(),
        name="remove_tag_from_interests",
    ),
]

polls_urlpatterns = [
    path("<str:survey_id>/", GetSurvey.as_view(), name="get_survey_by_id"),
    path(
        "<str:survey_id>/submit_answer/",
        SubmitAnswer.as_view(),
        name="submit_answer",
    ),
]

push_notification_urlpatterns = [
    path("", CreateNotifToken.as_view(), name="create_notif_token"),
]

V_0_0_0_urlpatterns = [
    path("auth/", include(authentication_urlpatterns)),
    path("oauth/", include(oauth_urlpatterns)),
    path("blog/", include(blog_urlpatterns)),
    path("events/", include(events_urlpatterns)),
    path("facilities/", include(facilities_urlpatterns)),
    path("profile/", include(profile_urlpatterns)),
    path("notifications/", include(notifications_urlpatterns)),
    path("website/", include(website_urlpatterns)),
    path("storage/", include(storage_urlpatterns)),
    path("categories/", GetCategories.as_view(), name="category_list"),
    path("polls/", include(polls_urlpatterns)),
    path("pushnotification/", include(push_notification_urlpatterns)),
]

urlpatterns = [
    path("V0.0.0/", include(V_0_0_0_urlpatterns)),
]
