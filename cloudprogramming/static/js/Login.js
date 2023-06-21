const loginBtn = document.getElementById('login-btn');
loginBtn.addEventListener('click', function(event) {
  // 이벤트 기본 동작(폼 제출)을 막음
  event.preventDefault();
  
  // 로그인 처리 코드
  
  // 다른 페이지로 이동
  window.location.href = "../template/Home.html";
});