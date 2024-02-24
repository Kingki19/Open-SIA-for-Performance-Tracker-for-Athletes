import streamlit as st

st.title('Open SIA (System Information Apps) Performance Tracker for Athletes')

data_profil_col, input_col, gambar_lokasi_sentra_col = st.columns(3)
fasilitas_col, preview_kegiatan_col, monitoring_evaluation_col = st.columns(3)

def create_container_in_column(col, label_button, image_link):
  with col:
    with st.container(border=True, height=150):
      st.button(label=label_button, use_container_width=True)
      st.image(image_link)

# with data_profil_col:
#   with st.container(border=True):
#     st.image('https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
#     st.write('Tekan ini untuk masuk ke data profil')

create_container_in_column(data_profil_col, 'data_profil', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
create_container_in_column(input_col, 'input', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHXmuJl-w2TCqnlKGBiVLB4StSjZBu4xa58A&usqp=CAU')
create_container_in_column(gambar_lokasi_sentra_col, 'gambar_lokasi_sentra', 'https://disk.mediaindonesia.com/files/news/2023/08/15/peta-indonesia-dan-38-provinsi.jpg')
create_container_in_column(fasilitas_col, 'fasilitas', 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoGBxMTExYUFBQYFhYZGyIaGxoaGiAgIRkcHB0fIiIfHx8cIisiIiEoIBwfIzQjKSwuMTExHCE3PDcwOyswMS4BCwsLDw4PHRERHTApIigwMDIwMDAwMDAuMDAwMDAwMDAwLjAwMDAwMDAyMDAwMDAwMDAwMDAwMDAwMDAwMDAwMP/AABEIAJ8BPgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAAIDBAYBBwj/xABDEAACAQIEAwUECAQFAwQDAAABAhEDIQAEEjEFQVEGEyJhcTKBkaEHFCNCUrHB8ILR4fEVM2JyoiSSskNjwuIWRFP/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/xAArEQACAgEDAwIGAgMAAAAAAAAAAQIRIQMSMQRBUSKBEzJhkaHwcbHR4fH/2gAMAwEAAhEDEQA/APKqOVP3jHTnOHUaR1QbyI3wwq/M2wpYXHLmMQZlquxEEwR05n1/riFFRjpAbUdgPyHvtiKrXJiRccxh+UAZxqYATc22G8Taek88CQJFgUlWCvzgz1/sRzHS/MxXZlM3k3JG53nfz6dMaft+eF93TOTqM1UQlQnZxoDaxHhBB8J023EWBwPr9mqtKlTkU3ZkFQqKqllUgEDQxEnqBJEXi2G0Noz9LYiLnn6Y6F8QU2kiecX6TcgcsXK1erSNSkRpBMMrIBdfWSpBm4OH8JegGBq0iwAY2Y+Nh7KmPZHKRJ2McsMo7m8gaNTwMrpIAcAgEwGIKuNVuci8Hli/2goUu7pkPSbMMTUqGmTADkm40qgIPhCrEROxBwFzNUM5KroIOwJMydgd9us/PDawMSRMgQfeRf10m2ASIXWJv6R+7Yai46wkyJ/f9cThNQYqehIMC+9r36/HpgGOyhW5YX0x7IjledwfSD53OGtH+79+WK89JjFjKZVnkqpMYAGIrMYAJO9sGqtIEKjeIgALqnlAi0WjnHTA/LJUpvcEaoBsJgkbTt64Nuwp7wLW93LzxjqSzghsiVxTWNAELBgTzm17cpxU+sl20i1777AeYkC/TnibiNZtJMLHQ+/4b4rcOpoGABJBBkkEeGI5/wCoRY8pMYUY2rBI5n6R0SLXAJHntPw/titlqjyovHIfr8cbr6Pkpu1dWy/eq6abgk07mWmYVbkyIO0HDKHBxljWTu6lSmwGktpkwFPiQAlYJeLzeYtOKtKIGbelUZ2dQToAm3s257evxxNw3NjTocFlNjB+PmMaGrGl+9y7KXka4ZZMWOwkgwbg9MBF4eqFzrBBnTuun3YzvFNCZqMnkKYowH0yZl0VvEViB4tUX+XuGizzZfO6aNfSgCqUqiAUcLBVweUr7POBe+MbwLjCO0MuqxAkwDaxnffltbCFcoTUgM24O+5mOh9Ok4UJyWJAmaqr2NrkrGZBYXd6kgrOwVbyAQeeBua4ZOUZTmFWoakhQwJcDm4AkWJ3MX5HHf8AG6tRUpmozKgnT3cEQNxpAttILYF8RpUzUu9VYPiQAAmIMWaQcaOcew7Roc/wSmyZZKdQNU8IOpibnTeYtBmCYtyOBOQz3cpVTvHksUNIEgyF0g2iBvsOcdTin3tKo+paz0lX7sSZHQgk/nzOKvEa6ioTqaoWJJZhpPK5bZvUH3Ye+8CstUszNSMwTSVrKwU+Ejqtpva5EYbQ7QfVapNF9axEsDfqQNryY3xLwjILmwdRpppl3q1GiPIaTLkyW2353wq/Y2omWGYZk0zEkkyGNiVgwIjzvtacPbgEgnwntrUrsUKysDwqDNtiQoJMHGmzfFq+VogjXUdl1eydCCLywAEyfxW88Zjh3ZN6VVMxSqAZcQzVQYCcyACAxI2EC5PLBbLUP8RzdRe9daaiCGMyuwCkmRq9NvmlGmNId2L47VqVfAQqiS6vIBMxINzPMzFzj0embDb3Yx2W7K18u4XL1Jo7kMYJLMZFt4Eb/PGuy1HQI1M3mxk40VlRslwsLCxRRW4jXCUnYtpABvBMe4XPux899pKJqVWfxaWYlLNfcG14IAJubBTj6HzWXWopVgGHQjHnOc4LmGztKklBVSmJZgCU0MxMyxu0Eyd9xJEnCqxMxvZvhuquoHd1RrCwdSiPxTAMTv5BpBx6TlOzeey9aqcvXQU3Aaag1EsZLWnmbk859wHdnewrZXOMSorULgajqKA+yb+0wEAmAb2mTjfVsxSpKNTJTGwkhR6D4beWBKsCUT5Optq3P5D5YjzCaTvPlj0HjHYTLZirR/w5yadRUZgRPdoSVLXhp8Oog3E9CAMPxHIvl670KwINNirARNjuOVxf34HFoVFOmJm4EAm/OOQ8zjgOJDSEWYehB/QRJ6TjlF2UgiRHPngGNJMfr6f3w8Neb7zvzHP1xPnatJlpinS0MqkO2onvDNmgkhbchb9KyjAMsr4gTPqSbnHUUaSwIkW9qDz2HPb8sQ6LTIwwNiRUbT6POzAz3fB0GhEP2pb/ACzpaJUsNSzNxcELeJByFSQpFje7b3A2Dc9/fA982X4i6atJIVvaS+lv9wESJvpNrCQcV3csSTuTJ9efp7sUMYahiJMdMTKWqFQ7wAIBN4AkxbzJHvxFywgOWACxn7aE1KwVbFWkXJMeRG0WxDTqkbbjEYGFgAJ5HPViSisZY+02olbeX8j+eJ1ru1RQWAtI2uT+yI/XAuh85B+GDnDGFQ66y6u7sBYCSCJYG1omcZTSWSA7lezVTMUwShh4VCWYDUxsRAYsItHnvgHxbL9zZkCNuAR7SknxAgDwmDB/vj0P6Nu1SU8tWVlXSCSi2B2sDz5C4B3HnDuKplM+7VkNMZoqmgPqhSntLZgGVl8MEbzMg4UdvFjxQE7IcGzoNLMUkamKkoGJK+FgWkGNJUwbHn7pm4tncxl61WhTqVGloc2AeJjSQNtwSd58sEOIcazGWp0suUWh9nA7uWV5MkgQAJMnbn6YCcQrVHBLP5SQNRBvHWfzn3YicoiZHxTi2Yd9NSo7gbKxLQB62wLzCWBIkTBFr77AeQIOIKhaWOowDG878oxHnKzwJBtz62MX2n+uCKYIWXqgHwjYzEfKPLF08TYKPASt7uJBI6SD5Yn4D2d7/uTOvvPu02WQbwj6o0s0HqIBxZ4XOVaoRWWlVpEgo/iEwVZQASCWsLyLbjnpsXcdAw8UqJPiOknw3PrAkbSd45YfTcVnVqlRxPhZyCRO1ySdhBjoOWLfGqVXNVqaCiKcUwFURamsnVG4kEtHMmwuMUW4X3Sp3qOGde8QD76GQp63Inl4QeZGDahUS5fI1FSpUUMioQGLKRCsDoJB5tB9OuEkmkVasTIhRrtuOTbCD8fnPkqahQ5qA1CpOh7aSDANyASQbb7Gwi5DNdm69ZlFChVCMAQCI1MB4mkgfuMAUM4bSal3Vao8GdCmlUQshWwBF4kdd4wQ7UcQrL3NGuETulnQAIgi1lkBmINvLAHi3C61B1oNfQJZBq+zJI3sBJtcSNr4N5PiWYQKGpLVpuNa/ZxYblGCi8dJEQBEYpAR8N4lXDgZukz0fZVQoU+K8rAk7ATe1sG+HdnDXqLXylUU6lJoKVCwcady4j2gT5DcWjFnsfRTPHvDmajd24Z6dQEgr90Ek6bHkuNzwrgVCgWalTClzJNz+frhqI0ibhVCqlMLVqCo43aIn3Yt4WFiyxYWFhYAFhRhYWABYr5nLayPERE7RzjqD0+eLGFgA8f7I8f4dl8zVqivV1uGLhwAp1lLjodRICjAX6ZcgKlZs3SUGkrJRdwLO5pyD5wBp1eajlj0bsr2Nyq5em9KmaTP9rqEFxrUiAzLMBWFoHzOIuG9m69bL57L16veU6rOiarspWAhnaJAaOW1ojFypiMj9E/ZvL52gzToamDTdRBl2B01DI6EQOTJIiSMUn+hnNrJarSCrrLMSQIX2TABsRfyuI54r/Q1x36nnmoVjoWsO7afu1EJ0zyFyy+8Y030t9sqtKk1ClUQrWBUMtyqzeGBi62956YiTQnR5Hw/JLWq6A6otzrYwAoO9zcwfZ3xFm6SozKralBIDRGoA7xJiY6nEtKUQPA35lb7gWN+R+WKzuzRqkxAHkMR3Gci2Oimeh3tgvXymWQUWSq1dmSXRRpZag+6dSxp87ki4xYokZdqb1XFZ9HhVG/yob2SRtIkmL89zgeEIC5rKmmxVjDCP2DhCizjUeVpjf4Ys5+qKzF/vRte3lJM4hWmwps2mVB0zOx/fPbCTbQiuwi2OBSBOHAfv8sWKOVLEp7Ni1+oE4dlFYEzJkjaevx/d8W8lwerV0lFlWcU9VgA0TBJsLdcOXI1gnskI3M2U6fFckxPONz8MEuzGSrOtQop0aCXJAghSJAY8/JbnaL4GAHbKlWA2Jg3tv8APBXhuXZGJDEqNyOnrfrg/k+xbVqkvroqwKljSYw0CQQDC+0IkiDvtibivZ9MqO571XZT42SmTEqIksNiLgAkb+eIlwQwLm80oOmnCiOVyfU2kDeMWsnXqNULeGmSVPJVGyzAWBtNus9cRUckWZXXU7ifZU3EAwPTeBFscTKMskkyOZBECSCINtwRNxNuRxmuACn16oQzF0k2DFpkXvfcW3jpiXI5BA4aqxqoSQqAFSzQIGoTztANz0wV7K8ByuYKVMw7lrsUVCAAJIkQTsDcRsOtzHGa1OkrmnnYW5WjoBAkwGWZMKCdp2MDGkdNcjozHGuEjLuxoqxolJ1L9qVaFMOfugWMESJG/Ilk8q9bIvUrUxRoUqJfUBequhioAW2nWJBIm5AjbB3shmatVz3lEFynjq1SQ0XIChUhVg8zNxMWGI+0mVq1cvmO6eki6XpgFyuvUBIBclSrREMBNoKxfVIdGBzyrl100xezpVVttKhakEQQJaYPVfUkc/wAMKlVAVFNgrCoIYsUVmBgG5ZoBBJseuC/aTtFQrZbLV6aaK8mpTSoIDCpTZDBbwuoYLsZtyYYM8AojLU/rFXOBaVVg8Ah1exZiC1wWZiYC2JPliWgaB+f4aMtlaVejTKZjutVRiIWmChBe3s2JM7tpg3uM9w/geZr1ldFerQqaqVNtZh6NE6SNdyqFlLA7+zAwf7R8QzGmcundVs5qgAh9VNRdixOlQEOra2rfYATQ40uXfL/AGb0qmWUjTVaddMrpXQLjUS+qBY8sOhkfHOB1snFRRS0U9KHWo1O7S5BH3rRf8LAYMdme1RNcvVqZgUXsakeEM19IgkBf9ajUYEQMCeJ9qKubWnSrUVaoKheVXQSxA/GTpUAEadzCyRcMSrcazq1ChT6qCpgKoSmsKW1KwkvaPU/DBjsB6RkVy9RAERGDDUQVubbtqEk7XPXGT7bcRejqVNVFSBTH2jaY1bBI0glfMQPXFPhPa/NVKSpTSnmmJKF7KzX3jUJsOnL3YNdos89I0u6Wmzv4ArqYUnaQDM3MA88MVg6hlq9KlTTLZekuXA8VZiv2iwT4lK+dje87TONLwHM1GYqO7NFRbSRqQ/gcAwD6frgPwftwWrtQzCpTZTDX0geZD3+B5i1jjU0crRZxXQKWIgOpkECeljub4ECLmFhYWGULCwsLAAsLCwsACwsLCwAVeHLFNREWFhFrDpbDODsDT1fidz8XbE2rRTJPIFvzOFkqOimijkoE+7fDYj57+l3hf1XidUqsLVisvSWnV/zU/HAPj/EDXNJiywU1aFWNBJIKnr7NjexHnjW/TqlX63TLuHHdlVhYCwZI6T4wYkkArMSJ8/QTiRIflKAMs20SPPE3EcxqZoRFkAAKICgDlN58ze+E8JKyZ0ix5Hn7r7dcEuCZKjUpqzEmXIaALKBMi/ribGCKIK+JTcXxYy1Bqkk+yDBJixMxg3n+CoNHcF6oZWLKFlkAeBMAmCBMkDHoHAvo0pU6dNy1OsSe8NIkw40+xqE7HSZC7gjngqxUebJwGtRIdqRIJIXnLbArHtQ3MTcYlr9mcyx0mjUDM4UFltLwyjX1IIaP7Y3mS4lkAKSv3lFNRpvrVWcEQyglFDKACpUyQQT4TvgtlGoDMrQZ2rZZkSpTDL7LgOwUmw0Kj6gImQotpGHtQUeR8S4A+WdqVUlWABI6iTEidjHuxNlawVw1HUGAAJPi1QN7DaRN5EDG9z1H69WNWmQmVpaaRaqGYFYLBzcMw1VCu5XTpMkGwvtRwenkmo1XSm0rqKBzYBpBRQdSg6jAZmm87RhOIUZHM8UqtQ+rsxKoQFLH2EjYDaNvgI64v8AZk2KuzBqaGrTBINMwwBLIWE2m4uDEcyI8rlRUV6rmp3rEVNrIJBkwJmLCI5emDdXgFXLV6ZqIVUwwqoCQVCyxAaNgbztHK0jYM03FeO162UqVDTTTMMKZbxER9pYaVM3ILczfGCq552s2lgPvGZAsYvytNupx6Dx/P8AfMDRhqdaloKsCpqkQDopSTqXwiQpF1uN8Dq3YfMOtMhEXRfQF1MQxJMtfUJA/h6ThSViaMU2bmCw09NAACtzsN9v3GL2Wzq0QXeGmCqS2liCbMoPiEk7874OZn6P6tJe9YoWeCtIfc1Tq1wbBTAkT7URacUsp2UatUdWzASuGIWiEbxaVDEBydN1JvseRIxOyQqNJ2a4zSzAUB2ptTGpqQRSBLQIbcoATIJEahFhaX6u9V1QZelTrZdp+1BVaitEAGDIHnPhbecA+DaMvnmWhRqs6nRpV1MX8SnwkMImDblPPG+p5bMHWGWmlPUCgcAa9Xt94BIJAMiIklsVF+Roy2YzFXLMtJFQ1CpCrSLKoFQlj7XiOkACbRAGBuayQKhCKlJBV1kCmDTFtcByxk6T7JAE/DBLiXD6gq64SquvwsFKvPPT4QQJaN7W/Dizksozt3AqVizoaa954hTFmIt/D4iJ8O2ByYGA4q1OnX0sJowalMARGs+IASNPiVwIAiVMYu8F45TpUyNSsaThqRqrJNIkzCDwltg3pbpjQ9qvo4qUqKV9ZzApnVVVbMac+MpvJ0++wN4jGSp8KypzQpPmB9WVXrCuBOunpUqpW3iBBQgX1ahGBJ9yjQ5XjtWua+cH2a06YRV0jRSoEwFsfaYyTA+6MU6mSqZuuuZzNYZdahGgEnvGVVgOqDUwkgXIA8UieZOn2cqV6TVHJo5R3D08uFGtgCArVUXTAjUQBtqvjV8J4VFWilLusu9MB6qqigOjBgIWT4xIBeTub8iwMdmeEOrpUoq5YVApNQakLj2QA51FiARLIATscaXjHAa9bL0ytJe9R9aUqgC6RA1DUWggjbmOUXxtsxw9SsC5mfENU8j7W0i3vnHnud7WPqfLvTeoklRAYNAuRpIPKwg7DlaHSQqOcO4fmMtQ+sProuSQwSoPFB8KlVGk2tqmdzuL5nh9Z6mYYB+9f21JaZPtRJIYWBEi5ONFXz9X6vUegAEQAADwkCNIldUytjMQSSd8C6OTp500xQp06dVjpZtYFgDJCi94325c8TJ1wSxcM4/Vq5pi60lWoDTIqJqU6d5M3a0Fp+Vseo9le9FLTUpU6SqYphDbTytA88eT5/s3XoKXcxVpkFSsEMCbQSQbRO3Me/bdmO2FSnoo51DTZhNNiANQESCBYEThqXkadcm7wsNRwRIw7FliwscOIxXAsSJwAS4WI++GH6x1GADuFhr1ALkgDzxF9cp/jHxn8sAGRq9rPs9FVgDCydEhpNwArTMA+V8Xcz2ionM0VDkIVYuSWEEadII2vPPGRzfZ1nZgQrrTcKW1FYMXMAXA1Dztjh7Nu1ZkBVdCBryZ1eW8wvPpjNNujTbFSf0V+4M+nRwyZR1qI6E1ICm+ptJc77TA8pGPLrjBTjtao50sZRGOi8jS5YgrJ2aLcoHngY6YpsyQey3ZWqKNDM1dPd1amlUmWcbk3sAeXWZtj0/sZPEaTLmssgosPBVpoKenREDUoG0Dy2EWOMp2urVe7yRDjSDU0WEaaYpqp26J88eidjeE0Fy4Q0KTd27Uw7U1LMFi7Ei5kn4YrbkeNtkVKrQyTjK5bMIkSzGsxO5BCKxGmNx7+ZnAjtHnOGvXJ70U6tRSTVSqGSnAIBOlwQ0mYWdpw+tkXOYqBKdDUioWBpIFbxv4QdJ0yIvB29+A+aywr0KivlkRHquNQWnqWD7ClRNo9r8sGOAhFzdIio8YybVFbMZmkzFHpNUCNUelEFHR2Xxr4GE3P2u8SBWOc4YWdBnqmlqlI6yHW2mr3vsiSrBhTvfxHlfFrL8JpU6Ay6KjRVVlLorEMxIMkiSLi20DDcpRVzRytShT1061bvtFNVANNazgTGpkqB6cA2Apxzw2qCUXF0w/2Y7UcLpal+toFJI0VJ0aV8CldQm6hTfl8s/2r45l85W+rtXpChTpO61FHtusikkzqJQMfCeYnxWwYocNZckpDKxKRZQNU1FANtvCDbzwI7UcPfMHKIQUd65pFgVMI9PxeztYGPScQ9SNpXliUZNWlhGx4LlMhWelVpVFFVoeqo1kVCQSQV1aQNTHkbADGgzrUKSpSOlaaqzmbwiFQVXzLOojmJG5xnsqHXMFUhVVVAA2Cg7Yk7QQ2YyQZh/muRtEii7DpzUG/NR0GLqiU34NLw2hANWqoWo/iMxNNfup/CN4tqLHnirxDibkxS9mPa5H4j8sNOZJHtXJ8uX6HAzP59VQtrDB5A0mbwYiOQi5vGJbSVsdSbpIBcS4Dma76HZmR3OltR8IBJhoANpMEyLi2DHZ3gmYy4BavrpkKr0qonQAIIBMkCLCDH5YbwbiwrUxqYIEch7zJHOSBF7wRti8aiPZaisTvDCT6XxMaktyY5QlF0+Qpw/LZWjBpIik8wL+87m/XDeMZqoVinTSpP4trXBg73H5YooumAdVp/fQ4snMLFwQRsW2M+h625YvFCqQJqLVpRVzDa7SqEhlUg/7VO1o2BAOBuUzGoPUKhC7Na5BkmDqvBuTHnjM/ShnMzVqBWZky1MAzSBIVjYM7A7TIgkXU+uD3YLia1ssaXerUdCZdhGtZlW0AkqeRg7i+Fs3ZFKL8hjIcTchUqeJSbgk3vy5z+eMlU7IZdOOJRIDUXQ1tAsJhvD6ahMe7a2Na+coU2VCVAgkqoZ3Am1kBOk9cZTiGbB4rl6yPCrSIYtqQqPtBqgw2mWExMT5TgCMa5N3SqUCzAUYAiCARNxvPPFnMcQyy1KYcUxUPhSY1HyX4beWMdl+1KtVpilDvUBZV1X8pJaAbMYnlvijxnheYq5ihWr0x/mKRpYQhD+CSJ0m4BtuCOYwJqr5KUXdPB6a2dRxHjHmJt8L4y3FezmtCKDEgOTA8OiVJJkGSZI+Vt5lzFGXILOxEQe8MX2tYcsdy3FWp6ySYHtzAAMbycDSY2gXxns6iCktNSAqywe2ogCBIEwWuZnlERilmOzlFkarSLUmiCFJgbzYHzwT4px9GUO1WmRMTp1qNjfQ1icCP8QpMSBXdQTEqnhiBc+KRJMe7EScO7Je0gpvWpU2Q1XqoqDSjSQF3J8zpmOkDpgb2Y4zrzVWixDUnUOocFlpnaF+9cQfdOL3FOJrRMy2mQsA6p1chJkiN5xkuM1CMyKdAvSLwPE0Tq522HK3Q40UI82dGnpKWm3f/D1btFmatLh9QU3EAQrUwTpAPQDYCxtjz76Pe2GZp5xA9VqlGpqpkQdEwSGsu4K+sE4K8A7RM1OpTrO61qQ0QGMHwkSItzn3AjGcfjr03U0mZQnsgGAALQAuwi2Mp6mx1ydPT9E9aDd1XH1PbE4kXIIqr6AfzxH2hou1NTT3U8j/AC54yfCONNWQMj1EHUtd/fHI/li4jxOp6pLdCpmeZkC/njWMoyjhnnyTTaaoqnjFVTp8WqYgrJJ6RNj88V6/GagOmp3gO8frbE1fNIGYxqYyQ0iZIi42n85wOoZekTK0mDeUb+gA5+uGkiHBo1vZ3M1K6Fqh1LPhad+v79cX0NJCRqZSbmZI91iB6DGZTOOoIDRMbt06AQB6i+GvmWN2bflePOLjEu+DSGOWIcUh9UnxGdK26yTa7f06YH5vjTBGYeFmGhP9RNlvM9SZ88RVeH5ktM0+URyvfcYiq8BzDEE1EEXELseox4ii7tsmvLMT22oKlVAnsimq7z7EgE+63uwC5Gd/6YucZr6qrnVrAOkN1C2n0O+Ka3aPL8xj1oJqCstHo3aGnTrnh2WD6dFFnfSRMuEgSZF4ONFxnj31bh4qr7VSoxtv4qjdDYxGBmW4RmFZajVE1IiqNYmAuwuMUc1kCTSpNUSoqAmIBA5CZF92xK193pSyzOUlVcFfiGdzAqZV3dA7sotN08B8TNuYN7bzh/F+OfV6YMtUQVnAWwgnxbgdMS8ZVGpMxRddMAoxAlSStltbkMZrtK32LXB/6hiD6Ig/XFR+ZNMcNRxlxX++4Ry/a+m9gjU2HiBJBHhki/8ATFbjucrQteFarUqo0BZIZVJ8QHtNFjMjpzxnsjSKO6uL+EEerKfyjHquV4TSUAhTq02JY2JHLlfEdR1EdLbu4fg6Fpy1nJrlAavxyuuWUkRo0qUWBJBJ1GNh4QYHnhnCOOtWFZzTg2ddJJ0upCgjmDpci3LVihxepKVj1q/+NIT/AMmOIOHZZfq1SQSHVZAMH/MY7/wjGbhBXLunSZOnObpcKroM5/jNRdJFRgSfFDGYBMjraNsCM321ZzALeFpRiSSpggsJ56T8ziWjwtK0MxqJdtmHSSfZGBmY4HQRiJqyOYK/0xtHqYyltXKJloTUVN8ML1OPZypQaqgqtTUNraTpgC5knlzwK4fxKrTy7KjsgWppARiBdWJiLQTBI54McC4kq0a2SCM2pGqAtUVJ1QCnTlMEwRIOKicMNPLu9YlSCSipoYSBaRsZO5sQCbYmU7bUvODSMNquOcfkfwnNa1l9wFJY/eJkSfOF/PDc4xraalBmimRJXwlWLDTExJO1pN/XEOQoVTTdmDDwgqwQRfYREnmbYG5bMM8agAmqNSrEQAT7PrilJO1F8GajOPzRu17/AMmn4txarQrCkalRvCCTJNyPxAwTvMDHf8WYjep7yf54AZjJipV0rWKhVHiIOljAJg7m55jkTzwZ4VkGmzUytM6nZgBr1ABVAYxHhY8jvtGNVPsZqDbKfEONtVpPT7xUR4U6g0SgJIiJkm89SfTEHYPJ5h6rd0PCo+0ctpSmOeomDIiYEnyxHxvKGnSvBPfGSL/dEXxsuF0/+nztEFVctVAkqstUGobW+9HwxWjq1fujSem+EVsrUddRcFWa8EmYi09LfnivxCoSwuSLEidlFoB8zy8ji3nqGYd2f7OWMwXXUBNhAJ5QJwI4bl8zXBdQqgixJhfCWUg9Ot/djNzVGLi8RLdDPkqwIAYLqViAIK3E8t4wXHamhVR6davpqEnYEKGiRDAEQGA3i4wAo8DzKI9SowXSjQUJOttBiTERzscZXh+QSrlsxVcMWpIhQg2BapDauvh288TDUjJc/rNdko0n3PTsvxsV6aEVKdTTYtTn2vvAyBzv79zhuaq+ExbAX6P8ir5TVTcBy7TItIgC/oB13xf4nRzCKQ9BieRWCp9DNvhh/FintsJQbW6gFnc0ulo02PiMXY8p5W9MV8lnCWuHKjeDJZY2BKnl1/liLOZasZ/6dzN/ErW9NLi3rizSq6W1pk6tNoglazD5EfLGWpXizOOmpPLDOjL1KSU11mW7xgNCHXpCidWkGBquCdyemGcXyrEBKdNnQQ2rWoKtMtphomeZnFHKcXdZmnXWetQNH/cv5YM5PP8AfBiAVi1yTNhe5tv6Y4tbV1NJJpHqdMoO4p9gPUyp0M1Tuix+ylWEgzPi0mBAH/LGZzFFkdkLTBj3Y1HHeJZqmw0Myrp5AkHzJg+K0b7YFVu0mYYLrCPIj7Smpv7xO18bwUpJNVn6m3T60NG4Oy32V4sKTqrmxNrm3r5Y3B4ipMKZ/XHlaMSxYx6AAR8LY0vDuKBd2cj0JA9Mdmn6MNnn9ZOM9TelV/tkWbYpUf2u8WopUgiIDtq1X/DoYHyxu6dSQCByx5txTjKtVP2bgtAvG8Dz9MaHhfGUZwr1CppAQBMao3JG5HTYeZw4SabtE9Q4PTjKLt914NQamB/EuNLSYKVYkibR+pGKfCOOpUpaqjqGDFTJiSCeWH5uolWIZGjqRjVyxhnFyQZrtymowjHoZn/44Bca7Z5mqjU0lQQQSAgsbR4RPlOBi0vP5fzwjT1eG552GORaUVwjrwBWyTDc44tCDIm388aJeEsfuR6n9N8TU+CjmflP54vIYKQ43XYkuwIPKLD0jBLgedLVGBsdIsTFgfP1xIOGUxvJ+XyxDX4edeqkAsKANwQZJJkdbDblhKKTsTSaqi7xatqell1BLVKilrzCK36nT7hgB2hyzmmU0yxqM0C+6oOXmDvi5k8jmUrrWhGYNqljItytf4Ys1+HZqq2qpUExphZAjoBsMJtqSqqFCCv1AHOZaa9ZyToBMHbUQLDbkfyGNFkeMg0SlTNKlQEaT4iNIDDkLg+ExM9cMp9myzanYtaDJ3+GL9PgFIfdGI1IKaW7t9DaMq+XHuDOJ0U+rqKVQVblmZZ3fTJJYCCSJjzxf4Pweo2XiHJbR7JUxGs2gmB4hvii+UbL06jVSoFQxpWSFAFuU+VsFuH5PSiAER7XvYXHxvjP4cqq+95OprRUbTzVUS5bKaPCyuum0MRJvJNv3fDjw6mZJDX/ANR/TE1OgOQj0GLFGiZ8KyfSflhw046bcu7MJ6kppR7IE1ezeXdtRVidOn2jtMxG2+KFbs7Sok1ElUpqzlZks0H5RONcvCarbrH/AB+W/wAsKr2eLKQXEbESQPTbFS1YLligpxe6PJn8plF+rAqxAZdQ6ixaPy+JxmOEZHWqnVBeoaY6CyX95aMb7M8INOiwAhFRoIuNoAn0GMpwPKKcm1W+pKwi52mnP98RpNNSlHz/AEabpS1o7vGfcL0Oy1U01cEXANwRy6xgrwnIvQUqBTLVILlmiyzAGxG8yJ3wRyFRqaBEZ9I2BYmB0ucCOM5ZqrFgotpi4tDEsLg7iBN9sbuU16o1ZilG6YF7ZS9J3gKvgJuCJYgTI5QOWO/Ugr66tRKYJVpZTc3FogQRFp3GLPaLLa8q1NAWqHSRMTZgTcADEHbGirUadQNGjSugC1zJJPliIp1nm3+S1qQU26xS/AePDWqqRTrrUpg6g2jT4og35xGBvZXhNStlaZ1U9BL2b/ew6eWNRwDhtGjRYNUL76QFZIEdCxuTzxU7AJR/w+gWB1eOSD/7j+cbYcoqSpoxlidxZWqcIcKQGpTykMB/TGQ4ZwRaHfZeuafeFFdCrEydc6VuAbC4I5Y9Jq5Wkb66o/iH8sZrjvCMscwX1FnSg1RUn/MqBoVZA5gkfDCjBRTUUU+VZW+izLfYV10qNNdl8YMwAsixA/PGzp5QKIB+FvkLYbwHgeWRSUYRUOuHYnSTuBJnc3knBVOFoLrH8JJ/XFOMW7oE5JUZLPrmS8qlRV8hy6+uK4fMDd3HqB+oxuVonr7iv9MPpmN//HEuHhmTg2+TCnO1T96TtEL88Z/tVxutRZGAQ6gQZX8MREEfix622SpPeB8Bjz36aeHolKgygyHYE+TL/wDXbE/D3YllC9cPVFkXAc+9ShTcpTEi8Ajmecz88Rdpc3Wp0xVUrZoNibEH8ZPy64I/Rxwvv8ijBmUqzKbAgwxNp9fiMaL/APGanN1Ycpn+uE9OnwVHU1Lttnk9fidR0IISDzVADHkwuMafsTk6TUu8cVKjCVhqhKxIIIWDBgi/mcU/pG4E2Xro33KgGxMSPCR8NJ9+NN2O4e9TKoQrEAsohgLA+uHJ1Goo01E5RUijxejSNOoPqoBKMA2q4JWx9nkY+GGcCOXajSYZUFmRSxFpMXPxxocxwVz92p7r/ngR2SyLfVhIc6XenEHdKrLy9MTvlWUcru8gjs2cutTNU6lAnTWLKLWVxIU3HT54OLUyo/8A1qvuZY/8sUeH8OC5/MJpaGpUqgAkH7ynBf6rG2pf1+eCc/oCwY7K9mDThswY/wBK/qbfLBCjRpqIUD3f0GKGYzXdqWieXriCn2hSYKsPS/5Y6nJJ0aKSYUdPLHO564r5fi1J7agp6Gxxfp05525YLsqvBCtFZviZaSfsYlWgOeH9z5gfvywqKshIHKcPC+WJdAw5ac7A4VBuIYwihOLNOmTYCcR183RpnxOCeiXPx9kfE4ynqwhyzSEJT+VAriXBmrqEJgBtU7nna/rgnk8lpsyhh1kj5BhhtHims/ZUJH4qjW+UYutn6qIxVVLgSFUBdR6S35nGXx5TXpi/fBo9JQfqa/sK5DLU/wD+AA6m/wAmOIeJUtbDumRQoiFTWSSdyFkCBtPXlhqV2qKrlEBI8YZpCkdNXh+WBHafiFAU9NXNugBAYUvavJCiBAmD93YHHI9XU1JbXj8m0YxgtwQ0V6YAFQPcatRnRP8Api3xxMeIKDpdWXlqVWZf+N/eScBOyjJo05ehVWi5YtVqMdRYAQb2IbyHLbHatXvLLVk9FdD8tQPywkoK020/4KuTppL7h9yQCwIiNwRB33bwj3GcDKmSpVcvUBCUg0zUSNM28bErTQn/AG9NzhmQ72kZUt56lYg/C3zwQy5RjaQ5uQ0sT/tNQmB5RiVJQfpfv/kdO7a4BFV6ygMKaVaWwqJVs0c/Zgek+84tUKQdQ0ETyMW+GCQokkiRMaW++0cwS3hjyjE1GiigKoAAsAuw8toHpjs0uo7S+5lqwi4+lUwdSySzsevlgL2/R/qzgIujwkvqgg6ttMeYvPPyxq+7wJ7YZQ1MnXUbhNQHXQQ36Y7EcTWGQ8P4oXDq34QR6G2LfZ7Id1l0pgyqlonoXYj3wcYzsrUbU9TxMpQAmDpDTMA7THTpjV9me0VHME0VDhlBYzYEAxNj58xjl0nP4ji3hI6NTY4KUVywucvO+Kx4JRLaikmIk9PywRvhbY6jAhpZJV2Ee4YuUUAviEnzw8NbfAAUp1/DGoDznb44xtTt01PM1KLliiNpV0UNrjezMAPWTgt/iCE8zeMWKL0m2ufTbCaN43FZWDj8XbMgLTDUVPtO8Bo6UxJufxbDzxlvpS4fl1yeukiK4qLLD2mBkeJtzy3ONetZQdpwF+kZEfh1aBDDQ3Pk64VUzOc7g0sIB/RZSDZZitY0ai1GAM2NlIBUmDubfCMbfIcXqMxpuqCqonSGs4/EhO6/MTBjGR+hGqO4zKHlUVvisf8Axxs+JcKpVrNTWQZBFj8RfBLEhaTTglIyfb7OLmUFKopoaGkPUiWMbKtpB6zy54K/RpxFHyq0gCHpltXhMGWJB1REkHbywG7RdgnqkFKriDKozM4X0JYEHzAwf4c2bpoq1BTbSoEjUC0CJNhf34SNZ7dqSNITgN2eoNSOZRhCmu7oeTK4VpH8RYe7Cp8WYG626Yt0+JUzu0eo/XFZRjhgbNsE4xQYf+rlqieppurD88aRm8sZntMR9a4fWUyBVekxHIVUgT5SuNF3J3BgdN8FiSyzwLM8WNUAFdImR6+uGUss17iPPD6NKmt5O87kfpi3TrD+H12tiXJMxuNZKgygBBLE+S2n3+mCWXzVRQApIA9/LEAiYjYb8/eTt/fDkDXEHygb7b/PEORDm+EaHIZzvBi8s4H8LymkBjuRtG2CUDG0brJvG6ycUYeXjkT5D+Z2wqYw+YwSVqilhlbMK7iCSqn7o235wSWtzOHUuGJPhRD5T/OTfE4g4fpHUY4pdGrtP7nTHqXVV9jqUo+4R7v0GJNK7GAfO354dIFgSPQ/ptjOv2jzBrtRXLfWFUwSV0EEGLk+DlIwtvURWMhu0m/VizSjTpIYGNwOvkJtfAXPl0tlsqr1C+pnqgkIYjUXqDTI2AU2ExizmeH95phqtBvvLTZGX36lIPuw3P5U6NNNqbttprsQGHMbb+7HNunF3Jc9spfvubVCSqL478nOFVMyVLVK1OtVvpCzoU7AFzeF3hV9+B+R7E0QweuzV3G0yqiOQEz8TgtwTJ1KVOGywQSfDTcMBflHI7xgggRgTL0wNy4gfG2N9HWjG219v1mOppttVmvrkalJAAAoAFhAiAMdqUwRaf8AuI/ngJm8zmGqlaUCkpE1G+8LSAu55ibD1wQoVGJ8sdj04SV0jLfJYsvsSRp9of6jv6kb+8YfRUgQIUHcLMfE3+EYroxx36x1xC6bTTuh/GlVWXRUxQ4/mgmXqkfhj/ut+uO1K1vXpgXxyhVrUiibmN/Ig/pjdGUuHQ7hNRKWWpIsH7MEjlJuTfzOJezNDuKQpi8EmfJmJj0k47wfhRCjXEi3XBRMsF6YO9hwqLFJrXw8YYFwguACQDyw/usNWqVxZo1154AMT2yymYZlNFKqaZ1NTJBaYiY3iOfXHOA9oCg0VqLK0AalBJcjr5+/nj0nLgRvOJKiBhBAI8xOI7nRHV9KjJWjDLTr5htb66NIeygOln82O4Hl+yzj+TqfVqo7xnp6ZKuoJtf2hFuszjXVuF0j7Ph/2n9NsUM/w1zTqUxDa0Zem4I8wd/LCpFLqHuVJUu1YMF2UydejWdMuEOumKhDkgQDE+GYIn540WY4nnKC95WpqaQ9pqTMWQdSGAkDnfAzsfV+rZkJW8BFHuyDyYOpEkWuBvjbtxOlt3qe4g/LEq6NdecVKlFVh/dA/L8QZlDq+pSJB3B9+JcnxQudLaQfwmxHuP5jGezVGpl3c5F/C/iai1ImmDzZWJAX0H9MA+03DOI5tFL0taIdQVNIIMG8DxbeeLvyjOMYLlqvez0ova6g+t/zwqdJD/6Q+GMB2J4sMsnd18u2oOSHYeIAxbxCYBn449DyGdSsupDbz3GGYzUVKkOWio2UD3Y6EA2HwxI2G7Ykk8KUW25EDnP7JxKlMm8Egedvl/fDKdEEyDM9RY9P3GLCUyfMxHpMCN9sZuVHDY5aBNy0kQI2ufPpEnF/hWTdzsNI6E74gocKVnh2MC6gdAflbGhypFMBVERi4R7mmnp92dFAg/mMdAx0sSZOOk41NxwUkfyw4UScQtVIwjUaLHFConaFtP5WxXfOop64qZkk74qdzOJspIK9+pMi846mYPp6YF0pTb4YuZesGtz6csSUXDnbRIxlvpAJdaMCbsbei4N1FE73xHnct3hTvQWInTDREj1w1yTJWqRm+CZnN90KaOKaifGxOrcyI/QwNsaHhtJggU1HfTN2M7mbcgPIY4uSXkukeuCOWyyqMLavA02lyRhMTUzHPE6R09+JEQb4dANp5lumJadUOYjY8xjoUdMWEpHDJGd30nDkp9cWFoPzjEqqDh0BGixyw/VfEbqQbYQN4wgCGWyOoXw2tkWXYSRteMMoZ8pbp54mPEm3AEYTsdIrNl2iMcHh2nzxfp5+Rdfhh6stSwt5EYLCiGhmBtJGL1FwRvgZUyhWxPphlLNPStM+XlhtXwCdBWrl2N0b44zfabM1mUCWUL7WgkT59T6Y0OXzWtZ2PlgVxio91aIjfnGJouE9srMhk82hYjVqDCGM3MdZk2I2/LBLId1I1AagLFTBMdRPzxgeN8JY1qjFRJN4ONTwbiKgBe7VDABKjeOuBZOvXnBwvlv8GkeqDsT/ABXw6lVZSCOkWOIGKjcef9ox1tI2nF0efbCFDiAG4J8jBwSo5nUJgAeu3wxmmqnDqGZYbGMLaNSNEM7Eki3lyw9M6jbEHGdfiAm8j9+WJqdO0hhfywto7P/Z')
create_container_in_column(preview_kegiatan_col, 'preview_kegiatan', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
create_container_in_column(monitoring_evaluation_col, 'monitoring_evaluation', 'data:image/jpeg;base64,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')


st.caption('it just a prototype, made to finish final project of software development course')
