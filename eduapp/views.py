from django.views.generic import *
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
# Create your views here.


class ClientMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programs"] = Program.objects.all()
        context["org"] = Organization.objects.first()

        return context


class ClientHomeView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clienthome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = "home"
        context["sliders"] = Slider.objects.all()
        context["testimonials"] = Testimonials.objects.all()
        context["facilities"] = Facility.objects.all()
        context["events"] = Event.objects.all()
        return context


class ClientAboutusView(ClientMixin, TemplateView):
    template_name = "clienttemplates/aboutus.html"


class ClientContactUsView(ClientMixin, TemplateView):
    template_name = "clienttemplates/contactus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testform'] = RandomForm
        return context


class ClientCoursesView(ClientMixin, TemplateView):
    template_name = "clienttemplates/courses.html"


class ClientGalleryView(ClientMixin, TemplateView):
    template_name = "clienttemplates/gallery.html"


class ClientJoinUsView(ClientMixin, TemplateView, CreateView):
    template_name = "clienttemplates/joinus.html"
    form_class = JoinUsForm
    success_url = reverse_lazy("eduapp:ClientHome")


class ClientProgramApplyView(SuccessMessageMixin, ClientMixin, CreateView):
    template_name = "clienttemplates/joinus.html"
    form_class = ApplicationForm
    success_url = "/"
    success_message = 'Application successfully submitted'

    def form_valid(self, form):
        program_id = self.kwargs["pk"]
        program_obj = Program.objects.get(id=program_id)
        form.instance.program = program_obj

        return super().form_valid(form)


class ClientLoginView(ClientMixin, FormView):
    template_name = "clienttemplates/login.html"
    form_class = LoginForm
    success_url = "/clz-admin/"

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, "clienttemplates/login.html",
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


class ClientRegisterView(ClientMixin, TemplateView):
    template_name = "clienttemplates/register.html"


class ClientProgramDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/programdetail.html"
    model = Program
    context_object_name = "programobject"


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org'] = Organization.objects.first()
        return context


class AdminHomeView(AdminRequiredMixin, TemplateView):
    template_name = "admintemplates/adminhome.html"


class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class AdminSliderListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminsliderlist.html"
    queryset = Slider.objects.all().order_by("-id")
    context_object_name = "sliderlist"


class AdminSliderCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminslidercreate.html"
    form_class = SliderForm
    success_url = reverse_lazy("eduapp:adminsliderlist")


class AdminSliderUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminslidercreate.html"
    form_class = SliderForm
    success_url = reverse_lazy("eduapp:adminsliderlist")
    model = Slider


class AdminSliderDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminsliderdelete.html"
    success_url = reverse_lazy("eduapp:adminsliderlist")
    model = Slider


class AdminOrganizationDetailView(AdminRequiredMixin, DetailView):
    template_name = "admintemplates/adminorganizationdetail.html"
    model = Organization
    context_object_name = "organizationupdate"


class AdminOrganizationUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminorganizationupdate.html"
    form_class = OrganizationForm
    success_url = reverse_lazy("eduapp:adminhome")
    model = Organization


class AdminProgramListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminprogramlist.html"
    queryset = Program.objects.all().order_by("-id")
    context_object_name = "programlist"


class AdminProgramCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminprogramcreate.html"
    form_class = ProgramForm
    success_url = reverse_lazy("eduapp:adminprogramlist")


class AdminProgramUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminprogramcreate.html"
    form_class = ProgramForm
    success_url = reverse_lazy("eduapp:adminprogramlist")
    model = Program


class AdminProgramDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminprogramdelete.html"
    success_url = reverse_lazy("eduapp:adminprogramlist")
    model = Program


class AdminSemesterListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminsemesterlist.html"
    queryset = Semester.objects.all().order_by("-id")
    context_object_name = "semesterlist"


class AdminSemesterCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminsemestercreate.html"
    form_class = SemesterForm
    success_url = reverse_lazy("eduapp:adminsemesterlist")


class AdminSemesterUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminsemestercreate.html"
    form_class = SemesterForm
    success_url = reverse_lazy("eduapp:adminsemesterlist")
    model = Semester


class AdminSemesterDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminsemesterdelete.html"
    success_url = reverse_lazy("eduapp:adminsemesterlist")
    model = Semester


class AdminSubjectListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminsubjectlist.html"
    queryset = Subject.objects.all().order_by("-id")
    context_object_name = "subjectlist"


class AdminSubjectCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminsubjectcreate.html"
    form_class = SubjectForm
    success_url = reverse_lazy("eduapp:adminsubjectlist")


class AdminSubjectUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminsubjectcreate.html"
    form_class = SubjectForm
    success_url = reverse_lazy("eduapp:adminsubjectlist")
    model = Subject


class AdminSubjectDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminsubjectdelete.html"
    success_url = reverse_lazy("eduapp:adminsubjectlist")
    model = Subject


class AdminTeacherListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminteacherlist.html"
    queryset = Teacher.objects.all().order_by("-id")
    context_object_name = "teacherlist"


class AdminTeacherCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminteachercreate.html"
    form_class = TeacherForm
    success_url = reverse_lazy("eduapp:adminteacherlist")


class AdminTeacherUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminteachercreate.html"
    form_class = TeacherForm
    success_url = reverse_lazy("eduapp:adminteacherlist")
    model = Teacher


class AdminTeacherDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminteacherdelete.html"
    success_url = reverse_lazy("eduapp:adminteacherlist")
    model = Teacher


class AdminFacilityListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminfacilitylist.html"
    queryset = Facility.objects.all().order_by("-id")
    context_object_name = "facilitylist"


class AdminFacilityCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminfacilitycreate.html"
    form_class = FacilityForm
    success_url = reverse_lazy("eduapp:adminfacilitylist")


class AdminFacilityUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/adminfacilitycreate.html"
    form_class = FacilityForm
    success_url = reverse_lazy("eduapp:adminfacilitylist")
    model = Facility


class AdminFacilityDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/adminfacilitydelete.html"
    success_url = reverse_lazy("eduapp:adminfacilitylist")
    model = Facility


class AdminEventListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/admineventlist.html"
    queryset = Event.objects.all().order_by("-id")
    context_object_name = "eventlist"


class AdminEventCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/admineventcreate.html"
    form_class = EventForm
    success_url = reverse_lazy("eduapp:admineventlist")


class AdminEventUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/admineventcreate.html"
    form_class = EventForm
    success_url = reverse_lazy("eduapp:admineventlist")
    model = Event


class AdminEventDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/admineventdelete.html"
    success_url = reverse_lazy("eduapp:admineventlist")
    model = Event


class AdminTestimonialsListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/admintestimonialslist.html"
    queryset = Testimonials.objects.all().order_by("-id")
    context_object_name = "testimonialslist"


class AdminTestimonialsCreateView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/admintestimonialscreate.html"
    form_class = TestimonialsForm
    success_url = reverse_lazy("eduapp:admintestimonialslist")


class AdminTestimonialsUpdateView(AdminRequiredMixin, UpdateView):
    template_name = "admintemplates/admintestimonialscreate.html"
    form_class = TestimonialsForm
    success_url = reverse_lazy("eduapp:admintestimonialslist")
    model = Testimonials


class AdminTestimonialsDeleteView(AdminRequiredMixin, DeleteView):
    template_name = "admintemplates/admintestimonialsdelete.html"
    success_url = reverse_lazy("eduapp:admintestimonialslist")
    model = Testimonials
