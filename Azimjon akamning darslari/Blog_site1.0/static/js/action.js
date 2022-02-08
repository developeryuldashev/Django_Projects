function  setreaction(like,dislike){
    document.getElementById('like').innerHTML=like
    document.getElementById('dislike').innerHTML=dislike
}


function setreaction(id,react){
    url=`/reaction/${id}/${react}`
    request=new Request(
        url,{
            method:'GET',
            headers: {'X-CSRFToken': csrftoken},

        }
    )
    fetch(request)
          .then((response) => {
            return response.json();

          })
          .then((data) => {
            // console.log(data);
            setreactions(data.likes,data.dislikes)
          });
        }
