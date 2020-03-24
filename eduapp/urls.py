from django.urls import path
from .views import *

app_name = "eduapp"
urlpatterns = [
    path("", ClientHomeView.as_view(), name="clienthome"),
    path("aboutus/", ClientAboutusView.as_view(), name="clientaboutus"),
    path("contactus/", ClientContactUsView.as_view(), name="clientcontactus"),
    path("courses/", ClientCoursesView.as_view(), name="clientcourses"),
    path("gallery/", ClientGalleryView.as_view(), name="clientgallery"),
    path("joinus/", ClientJoinUsView.as_view(), name="clientjoinus"),
    path("program/<int:pk>/apply/", ClientProgramApplyView.as_view(),
         name="clientprogramapply"),
    path("login/", ClientLoginView.as_view(), name="clientlogin"),
    path("register/", ClientRegisterView.as_view(), name="clientregister"),
    path("program/<int:pk>/detail/", ClientProgramDetailView.as_view(),
         name="clientprogramdetail"),



    path("clz-admin/", AdminHomeView.as_view(), name="adminhome"),
    path("logout/", AdminLogoutView.as_view(), name="adminlogout"),
    path("clz-admin/slider/list/",
         AdminSliderListView.as_view(), name="adminsliderlist"),
    path("clz-admin/slider/create/",
         AdminSliderCreateView.as_view(), name="adminslidercreate"),
    path("clz-admin/slider/<int:pk>/update/",
         AdminSliderUpdateView.as_view(), name="adminsliderupdate"),
    path("clz-admin/slider/<int:pk>/delete/",
         AdminSliderDeleteView.as_view(), name="adminsliderdelete"),
    path("clz-admin/organization/<int:pk>/detail/",
         AdminOrganizationDetailView.as_view(), name="adminorganizationdetail"),
    path("clz-admin/organization/<int:pk>/update/",
         AdminOrganizationUpdateView.as_view(), name="adminorganizationupdate"),
    path("clz-admin/program/list/",
         AdminProgramListView.as_view(), name="adminprogramlist"),
    path("clz-admin/program/create/",
         AdminProgramCreateView.as_view(), name="adminprogramcreate"),
    path("clz-admin/program/<int:pk>/update/",
         AdminProgramUpdateView.as_view(), name="adminprogramupdate"),
    path("clz-admin/program/<int:pk>/delete/",
         AdminProgramDeleteView.as_view(), name="adminprogramdelete"),
    path("clz-admin/semester/list",
         AdminSemesterListView.as_view(), name="adminsemesterlist"),
    path("clz-admin/semester/create",
         AdminSemesterCreateView.as_view(), name="adminsemestercreate"),
    path("clz-admin/semester/<int:pk>/update/",
         AdminSemesterUpdateView.as_view(), name="adminsemesterupdate"),
    path("clz-admin/semester/<int:pk>/delete",
         AdminSemesterDeleteView.as_view(), name="adminsemesterdelete"),
    path("clz-admin/subject/list/",
         AdminSubjectListView.as_view(), name="adminsubjectlist"),
    path("clz-admin/subject/create/",
         AdminSubjectCreateView.as_view(), name="adminsubjectcreate"),
    path("clz-admin/update/<int:pk>/update/",
         AdminSubjectUpdateView.as_view(), name="adminsubjectupdate"),
    path("clz-admin/subject/<int:pk>/delete/",
         AdminSubjectDeleteView.as_view(), name="adminsubjectdelete"),
    path("clz-admin/teacher/list/",
         AdminTeacherListView.as_view(), name="adminteacherlist"),
    path("clz-admin/teacher/create/",
         AdminTeacherCreateView.as_view(), name="adminteachercreate"),
    path("clz-admin/teacher/<int:pk>/update/",
         AdminTeacherUpdateView.as_view(), name="adminteacherupdate"),
    path("clz-admin/teacher/<int:pk>/delete/",
         AdminTeacherDeleteView.as_view(), name="adminteacherdelete"),
    path("clz-admin/facility/list/",
         AdminFacilityListView.as_view(), name="adminfacilitylist"),
    path("clz-admin/facility/create/",
         AdminFacilityCreateView.as_view(), name="adminfacilitycreate"),
    path("clz-admin/facility/<int:pk>/update/",
         AdminFacilityUpdateView.as_view(), name="adminfacilityupdate"),
    path("clz-admin/facility/<int:pk>/delete/",
         AdminFacilityDeleteView.as_view(), name="adminfacilitydelete"),
    path("clz-admin/event/list/",
         AdminEventListView.as_view(), name="admineventlist"),
    path("clz-admin/event/create/",
         AdminEventCreateView.as_view(), name="admineventcreate"),
    path("clz-admin/event/<int:pk>/update/",
         AdminEventUpdateView.as_view(), name="admineventupdate"),
    path("clz-admin/event/<int:pk>/delete/",
         AdminEventDeleteView.as_view(), name="admineventdelete"),
    path("clz-admin/testimonials/list/",
         AdminTestimonialsListView.as_view(), name="admintestimonialslist"),
    path("clz-admin/testimonials/create/",
         AdminTestimonialsCreateView.as_view(), name="admintestimonialscreate"),
    path("clz-admin/testimonials/<int:pk>/update/",
         AdminTestimonialsUpdateView.as_view(), name="admintestimonialsupdate"),
    path("clz-admin/testimonials/<int:pk>/delete/",
         AdminTestimonialsDeleteView.as_view(), name="admintestimonialsdelete"),











]
