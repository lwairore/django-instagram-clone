from django.shortcuts import render, redirect
from homepage.models import Image, Follow, Comments
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def timeline_page(request):
    current_user = request.user
    following_user_ids = []
    all_follows = Follow.objects.all()
    all_comments = Comments.objects.all()
    following_no = Follow.objects.filter(user_id=current_user.id)
    posts_no = Image.objects.filter  
    comments_ = []
    for i in all_comments:
        comments_.append([i.comment, i.image_id])

    for i in all_follows:
        if i.user_id == current_user.id:
            following_user_ids.append(i.following_id)
    following = []
    for i in following_user_ids:
        following.append(Image.objects.filter(uploaded_by_id=i ))
        comments_.append(Comments.objects.filter(image_id = i))
    comment_final = []
    for comment in comments_:
        comment_final.append(comment)
    return render(request, 'timeline/timeline.html', {'following':following, 'all_comments':all_comments, 'following_no':following_no.count()})


@login_required(login_url='/accounts/login')
def comment(request, image_id):
    if request.method == 'POST' and request.POST['comments_user']:
        comments = request.POST.get('comments_user')
        new_comment = Comments.objects.create(comment=comments, image_id=image_id)
    return redirect(timeline_page)

def like(request, image_id):
    image = Image.objects.get(id=image_id)
    if image.liked == False:
        image.likes = image.likes + 1
        image.liked = True
        image.save()
    elif image.liked == True:
        image.likes = image.likes - 1
        image.liked = False
        image.save()
    return redirect(timeline_page)
