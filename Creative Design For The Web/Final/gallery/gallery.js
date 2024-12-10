document.addEventListener("DOMContentLoaded", () => {
  const galleryWrappers = document.querySelectorAll(".gallery-wrapper");

  galleryWrappers.forEach((wrapper) => {
    const scrollAmount = window.innerWidth * 0.2; // 10% of viewport width
    const scrollDelay = 2000; // Scroll every 2 seconds

    setInterval(() => {
      const currentScroll = wrapper.scrollLeft;

      // If at the end, reset scroll to the beginning
      if (currentScroll + wrapper.clientWidth >= wrapper.scrollWidth) {
        wrapper.scrollTo({
          left: 0,
          behavior: "smooth",
        });
      } else {
        wrapper.scrollBy({
          left: scrollAmount,
          behavior: "smooth",
        });
      }
    }, scrollDelay); // Scroll every 2 seconds
  });
});