import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import Post from './Post.js';
import NewPost from './NewPost.js';

const BASE_URL = '/'

function App() {

  const[posts, setPosts] = useState([])

  useEffect(() => {
    async function fetchPosts() {
      try {
        const response = await fetch(BASE_URL + 'post/');
        const json = await response.json();
        console.log(json);
  
        if (response.ok) {
          setPosts(json.reverse());
        } else {
          throw response;
        }
      } catch (error) {
        console.log(error);
        alert(error);
      }
    }
  
    fetchPosts();
  }, []);

  return (
    <div className="App">
      <div className='blog_title'>
          Open City Blog
      </div>
      <div className='app_posts'>
        {
        posts.map(post => (
              <Post post={post}/>
        ))
      }
      </div>
      <div className='new_post'>
        <NewPost />

      </div>
    </div>
  );
}

export default App;
