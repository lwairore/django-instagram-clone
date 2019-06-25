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
    # print('=>'*10, following.count())

    print('---->' * 30)
    print(all_comments)
    comments_ = []
    for i in all_comments:
        comments_.append([i.comment, i.image_id])
        print(i.comment, i.image_id)
    print(comments_)

    for i in all_follows:
        if i.user_id == current_user.id:
            following_user_ids.append(i.following_id)
    # print('*' * 10)
    # print('Following',following_user_ids, current_user.id)
    
    following = []
    for i in following_user_ids:
        following.append(Image.objects.filter(uploaded_by_id=i ))
        comments_.append(Comments.objects.filter(image_id = i))
    # print('-+=*' * 30)
    # print(comments_)
    comment_final = []
    for comment in comments_:
        # print(comment)
        comment_final.append(comment)
    # print(comment_final)
    # for i in comment_final:
    #     for j in i:
    #         print(j.comment)
        # for i in comment:
        #     print(i.comment)
    print('+' *30)
    print(following)
    for i in following:
        for j in i:
            print(j.image, j.image_name, j.id)
    return render(request, 'timeline/timeline.html', {'following':following, 'all_comments':all_comments, 'following_no':following_no.count()})
     
    # following_user_images = Image.objects.filter()

@login_required(login_url='/accounts/login')
def comment(request, image_id):
    # print('-+' * 30)
    # print(request.POST['comments_user'])
    # print(request.POST.get('comments_user'))
    # if request.method == 'POST' and request.GET['comments_user']:
    #     comments = request.GET.get('comments_user')
    print('-+' * 30)
    #     print(comments)
    if request.method == 'POST' and request.POST['comments_user']:
        comments = request.POST.get('comments_user')
        print(comments, image_id)
        new_comment = Comments.objects.create(comment=comments, image_id=image_id)
        # Follow.objects.create(user_id=trial, following_id=following_id)
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
